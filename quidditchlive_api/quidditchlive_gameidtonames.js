import chalk from 'chalk';
import fetch from 'node-fetch';
import io from 'socket.io-client';
import fs from 'fs'

(async function() {
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
    //log(getCurrentTime(), chalk.bold('Fetching from "'+'http'+(ssl?'s':'')+'://'+remote_server+'/getServerTime.php'+'"'));
    let server_time = await fetch('http'+(ssl?'s':'')+'://'+remote_server+'/getServerTime.php').then(function(response){return response.json();});
    //log(getCurrentTime(), chalk.bold('Server timestamp is '+server_time.timestamp));
    let stop=getTimestamp_ms();
    let diff=parseInt((start+stop)/2-server_time.timestamp);
    //log(getCurrentTime(), chalk.bold('Time difference between local and server time is ')+chalk.bold.blue(diff+'ms')+chalk.bold('. '+(diff>0?'The server lags behind.':'Your local machine lags behind.')));
    return diff;
  }
  
  /*********************/
  /*** SERVER + AUTH ***/
  /*********************/
  const debug = false;
  const remote_server = debug?'localhost':'quidditch.live';
  const ssl = !debug;
  //log(getCurrentTime(), chalk.bold('Remote server is "')+chalk.bold.blue(remote_server)+chalk.bold('".'));
  const config = await fetch('http'+(ssl?'s':'')+'://'+remote_server+'/getStreamingSettings.php').then(function(response){return response.json();});
  const socket_address = config.socket_address;//'https://quidditch.live/api';//
  //const socket_port = 443;//config.socket_port;
  const auth_file = 'Input/Auth.txt';
  const gameid_file = 'Input/GameIDs.txt';
  const delay = 10; // delay of gametime loop execution in milliseconds (=maximum time resolution)
  
  /************************/
  /*** SCRIPT VARIABLES ***/
  /************************/
  var public_id, auth;
  var graphics = {};
  var teamnames = {};
  var saved_data = {};
  var diff = 0;
  var scores = {};
  var scores_str = "";

  /**********************/
  /*** INITIALIZATION ***/
  /**********************/
  async function getAuth(auth_file)
  {
    let auth;
    let from_file=true;
    try
    {
      auth=fs.readFileSync(auth_file, 'utf8');
    }
    catch(err)
    {
      from_file=false;
      //log(getCurrentTime(), chalk.bold.yellow('You can simplify authentication by creating a file "auth.txt" that contains only your authentication code and placing it in the Input folder.'));
      auth = readlineSync.question(getCurrentTime()+chalk.bold(' Auth? '));
    }
    if(auth)
    {
      //log(getCurrentTime(), chalk.bold.green('Authentication read'+(from_file?' from file':'')+'.'));
      return auth;
    }
    else
    {
      log(getCurrentTime(), chalk.red.inverse('No authentication for score crawl provided. Exiting.'));process.exit();
    }
  }
  async function readGameID(gameid_file)
  {
    let gameid;
    let from_file=true;
    try
    {
      gameid=fs.readFileSync(gameid_file, 'utf8').split("\r\n");
    }
    catch(err)
    {
      from_file=false;
      //log(getCurrentTime(), chalk.bold.yellow('You can simplify Game-ID by creating a file "gameids.txt" that contains all the gameids and placing it in the Input folder.'));
      gameid = readlineSync.question(getCurrentTime()+chalk.bold(' Game-ID? '));
    }
    if(gameid)
    {
      //log(getCurrentTime(), chalk.bold.green('Game-IDs read'+(from_file?' from file':'')+'.'));
      //log(gameid);
      return gameid;
    }
    else
    {
      log(getCurrentTime(), chalk.red.inverse('No Game-IDs for score crawl provided. Exiting.'));process.exit();
    }
  }
  /*************************/
  /*** SOCKET CONNECTION *** ==> only complete data sets are pushed due to no_delta being true
  /*************************/
  async function createSocketConnection(auth, public_id)
  {
      if(public_id && auth)
      {
        //log(getCurrentTime(), chalk.bold("Quidditch Score Crawl connected."));
        let filenames = ['score_left.txt','score_right.txt','gametime.txt','connected.txt'];
        for(var ii=0;ii<filenames.length;ii++){try{fs.unlinkSync(filenames[ii]);}catch(err){/*nothing*/}}
        //log(getCurrentTime(), chalk.bold('Establishing connection with '+socket_address+'.'));
        const socket = io(socket_address);
        socket.on('connect', function()
        {
          socket.emit('auth', {auth: auth, games: public_id, no_delta: true});
          socket.on('complete', function(data)
          {
            //log(getCurrentTime(), chalk.bold.black.bgGreen('New data received.'));
            saved_data = data;
            //log(saved_data);
            //saveScoreData(saved_data);
            saveTeamnames(saved_data);
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
            //log(getCurrentTime(), chalk.red.inverse('Disconnected'));
            process.exit();
          });
        });
      }else{//log(getCurrentTime(), chalk.red.inverse('Both, game id and authentication must be set. Exiting. '));
        process.exit();
      }
  }
  
  /*************************/
  /*** NAME INFORMATION ***/
  /*************************/
  async function saveTeamnames(data) {
    if(data)
      fs.appendFile("quidditchlive_api/gameidstonames.txt", data.public_id + ": " + data.teams.A.name + " - " + data.teams.B.name + "\n", (err) =>
      {
        if(err){
          log(err);
        }
      });
  }
  /*****************/
  /*** EXECUTION ***/
  /*****************/

  auth = await getAuth(auth_file);
  public_id = await readGameID(gameid_file);
  diff = await syncToServer();
  createSocketConnection(auth, public_id);
})();