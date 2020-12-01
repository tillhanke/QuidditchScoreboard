(async function() {

  'use strict'

  const io = require('socket.io-client');
  const fetch = require("node-fetch");
  const chalk = require("chalk");
  const readlineSync = require('readline-sync');
  const fs = require('fs');
  const http = require('http');
  const svg2img = require('svg2img');
  const download = require('download-file')
  const log = console.log; 

  /**********************/
  /*** HELP FUNCTIONS ***/
  /**********************/
  function getCurrentTime(){let today = new Date();return today.getFullYear().pad(4)+'-'+(today.getMonth()+1).pad(2)+'-'+today.getDate().pad(2)+' @ '+today.getHours().pad(2)+':'+today.getMinutes().pad(2)+':'+today.getSeconds().pad(2);}  Number.prototype.pad=function(size){var s=String(this);while(s.length<(size||2)){s='0'+s;}return s;}
  function customSleep(milliseconds) {return new Promise(resolve => setTimeout(resolve, milliseconds));}
  function getTimestamp_ms(){return Date.now();}
  async function syncToServer()/*if result is positive, local time is ahead and server time lags behind*/
  {
    let start=getTimestamp_ms();
    log(getCurrentTime(), chalk.bold('Fetching from "'+'http'+(ssl?'s':'')+'://'+remote_server+'/getServerTime.php'+'"'));
    let server_time = await fetch('http'+(ssl?'s':'')+'://'+remote_server+'/getServerTime.php').then(function(response){return response.json();});
    log(getCurrentTime(), chalk.bold('Server timestamp is '+server_time.timestamp));
    let stop=getTimestamp_ms();
    let diff=parseInt((start+stop)/2-server_time.timestamp);
    log(getCurrentTime(), chalk.bold('Time difference between local and server time is ')+chalk.bold.blue(diff+'ms')+chalk.bold('. '+(diff>0?'The server lags behind.':'Your local machine lags behind.')));
    return diff;
  }
  
  /*********************/
  /*** SERVER + AUTH ***/
  /*********************/
  const debug = false;
  const remote_server = debug?'localhost':'quidditch.live';
  const ssl = !debug;
  log(getCurrentTime(), chalk.bold('Remote server is "')+chalk.bold.blue(remote_server)+chalk.bold('".'));
  const config = await fetch('http'+(ssl?'s':'')+'://'+remote_server+'/getStreamingSettings.php').then(function(response){return response.json();});
  const socket_address = config.socket_address;//'https://quidditch.live/api';//
  //const socket_port = 443;//config.socket_port;
  const auth_file = './auth.txt';
  const gameid_file = './gameid.txt';
  const delay = 10; // delay of gametime loop execution in milliseconds (=maximum time resolution)
  
  /************************/
  /*** SCRIPT VARIABLES ***/
  /************************/
  var public_id, auth;
  var graphics = {};
  var teamnames = {};
  var saved_data = {};
  var diff = 0;

  /**********************/
  /*** INITIALIZATION ***/
  /**********************/
  async function getAuth()//auth_file)
  {
    /*
    let auth;
    let from_file=true;
    try
    {
      auth=fs.readFileSync(auth_file, 'utf8');
    }
    catch(err)
    {
      from_file=false;
      log(getCurrentTime(), chalk.bold.yellow('You can simplify authentication by creating a file "auth.txt" that contains only your authentication code and placing it in the same folder as this script.'));
      auth = readlineSync.question(getCurrentTime()+chalk.bold(' Auth? '));
    }
    if(auth)
    {
      log(getCurrentTime(), chalk.bold.green('Authentication read'+(from_file?' from file':'')+'.'));
      return auth;
    }
    else
    {
      log(getCurrentTime(), chalk.red.inverse('No authentication provided. Exiting.'));process.exit();
    }
    */
    let auth = process.argv[2]
    if(auth) return auth;
  }
  async function readGameID()//gameid_file)
  {
    /*
    let gameid;
    let from_file=true;
    try
    {
      gameid=fs.readFileSync(gameid_file, 'utf8');
    }
    catch(err)
    {
      from_file=false;
      log(getCurrentTime(), chalk.bold.yellow('You can simplify Game-ID by creating a file "Gameid.txt" that contains only your gameid and placing it in the same folder as this script.'));
      gameid = readlineSync.question(getCurrentTime()+chalk.bold(' Game-ID? '));
    }
    if(gameid)
    {
      log(getCurrentTime(), chalk.bold.green('Game-ID read'+(from_file?' from file':'')+'.'));
      return gameid;
    }
    else
    {
      log(getCurrentTime(), chalk.red.inverse('No Game-ID provided. Exiting.'));process.exit();
    }
    */
    let gameid = process.argv[3]
    if(gameid) return gameid;
  }
  /*************************/
  /*** SOCKET CONNECTION *** ==> only complete data sets are pushed due to no_delta being true
  /*************************/
  async function createSocketConnection(auth, public_id)
  {
    if(public_id && auth)
    {
      process.chdir('quidditchlive_api');
      let filenames = ['score_left.txt','score_right.txt','gametime.txt','connected.txt'];
      for(var ii=0;ii<filenames.length;ii++){try{fs.unlinkSync(filenames[ii]);}catch(err){/*nothing*/}}
      log(getCurrentTime(), chalk.bold('Establishing connection with '+socket_address+'.'));
      const socket = io(socket_address);
      socket.on('connect', function()
      {
        socket.emit('auth', {auth: auth, games: [public_id], no_delta: true});
        socket.on('complete', function(data)
        {
          log(getCurrentTime(), chalk.bold.black.bgGreen('New data received.'));
          saved_data = data;
          //log(saved_data.events);
          saveScoreData(saved_data);
          savePenalty(saved_data);
        });
        socket.on('err', function(data)
        {
          if('msg' in data)
          {
            log(getCurrentTime(), chalk.red.inverse(data.msg));
          }
        });
        socket.on('disconnect', function()
        {
          log(getCurrentTime(), chalk.red.inverse('Disconnected'));
          process.exit();
        });
      });
    }else{log(getCurrentTime(), chalk.red.inverse('Both, game id and authentication must be set. Exiting. '));process.exit();}
  }
  
  /*************************/
  /*** SCORE INFORMATION ***/
  /*************************/
  async function saveScoreData(data)
  {
    process.chdir('..');
    process.chdir('Output');
    let score = await getScore(data);
    if(score===false){log(getCurrentTime(), chalk.bold.blue('No score data available.'));return true;}
    let score_before={A:null,B:null};
    let team_letters = ['A', 'B'];
    let team_sides = ['left', 'right'];
    for(var ii=0;ii<team_letters.length;ii++)
    {
      let team_letter=team_letters[ii];
      let team_side = team_sides[ii];
      try{score_before[team_letter] = fs.readFileSync('score_'+team_sides[ii]+'.txt', 'utf8');}catch(err){score_before[team_letter]='';}
      if(score_before[team_letter]!=score[team_letter])
      {
        fs.writeFile('score_'+team_sides[ii]+'.txt', score[team_letter], (err) => 
        {
          if(err){log(err);}
          else{log(getCurrentTime(), chalk.bold('Score is ')+chalk.bold.cyan(score.A+'-'+score.B)+chalk(' ==> saved to file "score_'+team_side+'.txt".'));}
        });
      }
    }
    process.chdir('..');
    process.chdir('quidditchlive_api');
  }
  async function getScore(data)
  {
    try
    {
      if(data['data_available'])
      {
        let points = {'A': 0, 'B': 0};
        let points_str = {'A': '0', 'B': '0'};
        for(var team in points)
        {
					let period_data = data.score[team].total;
					if(period_data!=null)
					{
						points[team]+=period_data;
					}
					if(period_data.snitchPoints!=null)
					{
						points[team]+=period_data.snitchPoints;
					}
					points_str[team] = points[team].toString();
        }
        for(var team in points_str)
        {
          let other_team=(team=='B')?'A':'B';

					let caught = data.score[team].snitchCaught;
					let caught_other_team = data.score[other_team].snitchCaught;
					if(caught!=null)
					{
						if(caught || caught_other_team)
						{
							if(caught){points_str[team]+='*';}
							else{points_str[team]+='°';}
						}
          }
        }
        return points_str;
      }
    }
    catch(err){log(err);}
    return false;
  }
  
  async function savePenalty(data)
  {
    let penalty = await getPenalty(data);
    if(penalty===false){log(getCurrentTime(), chalk.bold.blue('No penalty data available.'));return true;}
    let penalty_before = null;
    try{penalty_before = fs.readFileSync('penalty.txt', 'utf8');}catch(err){penalty_before='';}
    if(penalty_before!=penalty)
    {
      fs.writeFile('penalty.txt', penalty, (err) =>
      {
        if(err){log(err);}
      });
      let penalty_details = penalty.split(",")
      fs.writeFile('penalty_team.txt', penalty_details[0], (err) => 
      {
        if(err){log(err);}
        else{log(getCurrentTime(), chalk.bold('New penalty entry saved to penalty file "penalty_team.txt".'));}
      });
      fs.writeFile('penalty_card.txt', penalty_details[1], (err) => 
      {
        if(err){log(err);}
        else{log(getCurrentTime(), chalk.bold('New penalty entry saved to penalty file "penalty_card.txt".'));}
      });
      fs.writeFile('penalty_playername.txt', penalty_details[2], (err) => 
      {
        if(err){log(err);}
        else{log(getCurrentTime(), chalk.bold('New penalty entry saved to penalty file "penalty_playername.txt".'));}
      });
      fs.writeFile('penalty_playernumber.txt', penalty_details[3], (err) => 
      {
        if(err){log(err);}
        else{log(getCurrentTime(), chalk.bold('New penalty entry saved to penalty file "penalty_playernumber.txt".'));}
      });
      fs.writeFile('penalty_reason.txt', penalty_details[4], (err) => 
      {
        if(err){log(err);}
        else{log(getCurrentTime(), chalk.bold('New penalty entry saved to penalty file "penalty_reason.txt".'));}
      });
      fs.writeFile('penalty_teamname.txt', penalty_details[5], (err) => 
      {
        if(err){log(err);}
        else{log(getCurrentTime(), chalk.bold('New penalty entry saved to penalty file "penalty_teamname.txt".'));}
      });
    }
  }

  async function getPenalty(data)
  {
    try
    {
      if(data['data_available'])
      {
        let penalty_str = ""
        let last_penalty = data.events.penalty[data.events.penalty.length-1]
        if(typeof last_penalty === "undefined") return false;
        penalty_str = (last_penalty.team + ","
                    + last_penalty.color + ","
                    + last_penalty.player_name + ","
                    + last_penalty.player_number + ","
                    + last_penalty.reason + ",");
        if(last_penalty.team == "A")
          penalty_str += data.teams.A.name;
        else if(last_penalty.team == "B")
          penalty_str += data.teams.B.name;
        //log(penalty_str)
        return penalty_str;
      }
    }
    catch(err){log(err);}
    return false;
  }
  
  /*****************/
  /*** GAME TIME *** ==> latest after 30 seconds you realize if you aren't connected to the timekeeper anymore
  /*****************/
  function getGameTimeString(obj, gameduration){
		let gametime;
		gametime = gameduration;
		let minutes = parseInt(Math.floor(gametime/1000/60));
		let seconds = parseInt(Math.floor(gametime/1000-minutes*60));
		return minutes.pad(2)+":"+seconds.pad(2);
	}
  function getFirstOTGameTimeFromGameDuration(obj, gameduration){let time_left = obj.gametime.firstOT.periodLength_ms-gameduration;let gametime = Math.ceil(time_left/1000)*1000;if(gametime<0){gametime=0;}return gametime;}
  function getFirstOTGameDuration(){let period_gameduration;if(saved_data.gametime.firstOT.running){period_gameduration = saved_data.gametime.firstOT.gameDurationLastStop_ms+(getTimestamp_ms()-diff)-saved_data.gametime.firstOT.timeAtLastStart_ms;if(period_gameduration>saved_data.gametime.firstOT.periodLength_ms){period_gameduration=saved_data.gametime.firstOT.periodLength_ms;}}else{period_gameduration = saved_data.gametime.firstOT.gameDurationLastStop_ms;}return period_gameduration;}
  async function gametimeLoop(delay){
    let last_gametime_str = '';
    let gametime_str = '';
    let last_connected;
    while(true){
    await customSleep(delay);
    if(Object.keys(saved_data).length!=0){
      try{
				let period_gameduration;
				if(saved_data.gametime.running){
					period_gameduration = saved_data.gametime.last_stop+(getTimestamp_ms()-diff)-saved_data.gametime.last_start;
				}
				else{
					period_gameduration = saved_data.gametime.last_stop;
				}
        let gametime_str = getGameTimeString(saved_data, period_gameduration);
        if(gametime_str!=last_gametime_str){
          last_gametime_str = gametime_str;
          process.chdir('..');
          process.chdir('Output');
          fs.writeFile('timer.txt', gametime_str, (err) => {
            if(err){
              log(err);
            }
            else{
              log(getCurrentTime(), chalk.bold('Gametime is ')+chalk.bold.blue(gametime_str)+chalk(' ==> saved to file "timer.txt".'))
              ;}
          });
          process.chdir('..');
          process.chdir('quidditchlive_api');
          }
				/*
        if('alive_timestamp' in saved_data){
          let delta_from_last_alive_ms = ((getTimestamp_ms()-diff)-saved_data.alive_timestamp*1000);
          let connected = delta_from_last_alive_ms<30000;
          if(connected!==last_connected){
            last_connected=connected;
            fs.writeFile('connected.txt', connected, (err) => {
              if(err){
                log(err);
              }
              else if(connected){
                log(getCurrentTime(), chalk.bold('The timekeeper is currently ')+chalk.bold.green('connected')+chalk(' ==> saved to file "connected.txt".'));
              }
              else{log(getCurrentTime(), chalk.bold('The timekeeper is currently ')+chalk.bold.red('not connected')+chalk(' ==> saved to file "connected.txt".'));}
            });
          } 
        }
				*/
      }
      catch(err){log(err);}
      }
      }
    }
  
  /*****************/
  /*** EXECUTION ***/
  /*****************/
  auth = await getAuth();//auth_file);
  public_id = await readGameID();//gameid_file);
  diff = await syncToServer();
  gametimeLoop(delay);
  createSocketConnection(auth, public_id);
})()