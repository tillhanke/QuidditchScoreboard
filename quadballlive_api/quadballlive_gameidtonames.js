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
let gameid_file = 'GameIDs.txt';
let diff_to_server_ms = 0;


/**********************/
/*** INITIALIZATION ***/
/**********************/
async function read_game_id(gameid_file) {
  let gameid;
  try {
    gameid = await fs.readFile(join( __dirname, '../Input/'+gameid_file), 'utf8');
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
    
    log( chalk.green.inverse( 'Connected with API for GameIDstoNames' ) );

  })
  .on( 'connect_error', function( data ) {
    
    log( chalk.red.inverse( data ) );
    process.exit();

  })
  .on( 'games', async ( games ) => { // initial data
    
    if( games.length === 0 ) {
      log( chalk.red.inverse( 'No game with id "' + game.id + '" found. Exiting.' ) );
      process.exit();
    }
    save_teamnames( games );

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
/*** NAME INFORMATION ***/
/*************************/
async function save_teamnames(game) {
  if(game) {
    game.forEach(element => {
      fs.appendFile(join( __dirname, "gameidstonames.txt"), element.id + ": " + element.team.a.name + " - " + element.team.b.name + "\n", (err) => {
        if(err)
          log(err);
      });
    });
  }
}

/*****************/
/*** EXECUTION ***/
/*****************/
fs.writeFile(join( __dirname, "gameidstonames.txt"), "");
diff_to_server_ms = await sync_to_server();
game_id = await read_game_id(gameid_file);
create_socket_connection( code, game_id );