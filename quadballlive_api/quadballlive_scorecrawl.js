import io from 'socket.io-client';
import chalk from 'chalk';
import fs from 'fs/promises';
import { host, code } from './env.js';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import _ from 'lodash';
import { 
  log, 
  sync_to_server
} from './utility.js';

const __dirname = dirname( fileURLToPath( import.meta.url ) );

/************************/
/*** SCRIPT VARIABLES ***/
/************************/
let game_id;
let game;
let gameid_file = 'gameids_scorecrawl.txt';
let diff_to_server_ms = 0;
var scores = {};
var scores_str = "";
var a_caught, b_caught;

/**********************/
/*** INITIALIZATION ***/
/**********************/
async function read_game_id(gameid_file) {
  let gameid;
  try {
    gameid = await fs.readFile(join( __dirname, gameid_file), 'utf8');
    gameid = gameid.split("\r\n");
  }
  catch(err) {
    log(err)
  }
  if(gameid)
    return gameid;
  else
    log( chalk.red.inverse('No Game-IDs for score crawl provided. Exiting.'));process.exit();
}

/*************************/
/*** SOCKET CONNECTION ***
/*************************/
async function create_socket_connection( code, game_id ) {
  
  if( !game_id || !code ) {
    log( chalk.red.inverse( 'Both, public game code and code must be set. Exiting.' ) );
    process.exit();
  }

  io( host, { auth: { code, game_ids: game_id, send_initial: true } } )
  .on( 'connect', function() {
    
    log( chalk.green.inverse( 'Connected with API for ScoreCrawl' ) );

  })
  .on( 'connect_error', function( game ) {
    
    log( chalk.red.inverse( game ) );
    process.exit();

  })
  .on( 'games', async ( games ) => { // initial game
    
    if( games.length === 0 ) {
      log( chalk.red.inverse( 'No game with id "' + game.id + '" found. Exiting.' ) );
      process.exit();
    }
    save_score_game( games );

  })
  .on( 'game', ( g ) => { // updates
  
    game = g;
    save_score_game( game );

  })
  .on( 'error', ( err ) => {
    
    log( chalk.red.inverse( 'Error: ' + err ) );

  })
  .on( 'disconnect', function() {
    
    log( chalk.red.inverse( 'Disconnected' ) );
    process.exit();

  });
}

/*************************/
/*** SCORE INFORMATION ***/
/*************************/
async function save_score_game(game) {
  if (!Array.isArray(game)) {
    a_caught = game.score.a.snitch_caught?"*":""
    b_caught = game.score.b.snitch_caught?"*":""
    scores[game.id] = game.team.a.name + " " + String(game.score.a.total) + a_caught + ":" + String(game.score.b.total) + b_caught + " " + game.team.b.name;
  }
  else if (game.length > 0) {
    game.forEach (element => {
      a_caught = element.score.a.snitch_caught?"*":""
      b_caught = element.score.b.snitch_caught?"*":""
      scores[element.id] = element.team.a.name + " " + String(element.score.a.total) + a_caught + ":" + String(element.score.b.total) + b_caught + " " + element.team.b.name;
  })}
  else {
    return
  }
  
  scores_str = "";
  Object.keys(scores).forEach(key => {
    scores_str += scores[key] + " | ";
  });

  fs.writeFile("Output/ScoreCrawl.csv", "Scorecrawl\n"+scores_str, (err) => {
    if(err)
      log(err);
  });
}

/*****************/
/*** EXECUTION ***/
/*****************/
diff_to_server_ms = await sync_to_server();
game_id = await read_game_id(gameid_file);
create_socket_connection( code, game_id );