import io from 'socket.io-client';
import chalk from 'chalk';
import fs from 'fs/promises';
import { host, code } from './env.js';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import _ from 'lodash';
import { 
  log, 
  sleep,
  get_timestamp_ms,
  sync_to_server
} from './utility.js';

const __dirname = dirname( fileURLToPath( import.meta.url ) );

/*********************/
/*** SERVER + CODE ***/
/*********************/
log( chalk.bold( 'Remote server is ' ) + chalk.bold.blue( host ) + chalk.bold( ' .' ) ); 
const delay = 10; // delay of gametime loop execution in milliseconds (=maximum time resolution);

/************************/
/*** SCRIPT VARIABLES ***/
/************************/
let game_id;
let overtime_written = false;
let game;
let diff_to_server_ms = 0;
const filenames = [
  'ScoreLeft.txt',
  'ScoreRight.txt',
  'Gametime.txt',
  'OvertimeSetscore.txt',
  'connected.txt'
];

/**********************/
/*** INITIALIZATION ***/
/**********************/
async function readGameID() {
    let gameid = process.argv[2]
    if(gameid) return gameid;
}

/*************************/
/*** SOCKET CONNECTION ***
/*************************/
async function create_socket_connection( code, game_id ) {
  
  if( !game_id || !code ) {
    log( chalk.red.inverse( 'Both, public game code and code must be set. Exiting.' ) );
    process.exit();
  }
    
  // deletes files if they exist already
  for( const filename of filenames ) {
    try {
      await fs.unlink( join( __dirname, filename ) );
    }
    catch( err ) {
      /*nothing*/ 
    }
  }

  // connecting to api
  log( chalk.bold( 'Establishing connection with socket.io ...' ) );

  io( host, { auth: { code, game_ids: [ game_id ], send_initial: true } } )
  .on( 'connect', function() {
    
    log( chalk.green.inverse( 'Connected with API' ) );

  })
  .on( 'connect_error', function( data ) {
    
    log( chalk.red.inverse( data ) );
    process.exit();

  })
  .on( 'alive', ( g ) => { 
    
    log( chalk.gray( 'Game is alive' ) ); 
    game.alive_timestamp = g.alive_timestamp;
  
  })
  .on( 'games', async ( games ) => { // initial data
    
    if( games.length === 0 ) {
      log( chalk.red.inverse( 'No game with id "' + game.id + '" found. Exiting.' ) );
      process.exit();
    }
    game = games[0];
    save_score_data( game );
    save_penalty_data( game );

  })
  .on( 'game', ( g ) => { // updates
    
    log( chalk.bold.black.bgGreen( 'New data received.' ) );
    game = g;
    save_score_data( game );
    save_penalty_data( game );

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
async function save_score_data(game) {
  let score = await get_score(game);
  if( score === false ) {
    log( chalk.bold.blue( 'No score game available.' ) );
    return true;
  }
  let score_before = {
    left: null,
    right: null
  };
  let sides = ['a', 'b'];
  for( const side of sides ) {
    let pos = ''
    if (side == 'a')
      pos = 'Left'
    else if (side == 'b')
      pos = 'Right'
    try {
      score_before[side] = await fs.readFile( join( __dirname, '../Output/Score' + pos + '.txt' ), 'utf8' );
    }
    catch( err ) {
      score_before[side] = '';
    }
    if( score_before[side] === score[side] ) continue;
    try {
      await fs.writeFile( join( __dirname, '../Output/Score'+ pos + '.txt' ), score[side] );
      log( chalk.bold( 'Score is ' ) + chalk.bold.cyan( score.a + '-' + score.b ) + chalk( ' ==> saved to file "Score' + pos + '.txt".' ) );
    }
    catch( err ) {
      log( err);
    }
  }
}

async function get_score( game ) {
  try {
    if( game.game_over == null ) return false;
    let points_str = {
      a: game.score.a.total.toString(),
      b: game.score.b.total.toString()
    }
    for( let side in points_str ) {
      let other_side = ( side === 'b' ) ? 'a' : 'b';
      let caught = game.score[side].snitch_caught;
      let caught_other_side = game.score[other_side].snitch_caught;
      if( !caught && !caught_other_side ) break;
      else if( caught ) {
        points_str[side] += '*';
      }
      else if( caught_other_side ) {
        points_str[side] += '';
      }
    }
    return points_str;
  }
  catch( err ) {
    log( err);
  }
  return false;
}


/****************************/
/*** PENALTY INFORMATION ***/
/**************************/

async function save_penalty_data( game ) {
  
  let penalty = await get_penalty_data( game );
  if (penalty === false) {
    log(chalk.bold.blue('No penalty data available.'));
    return true;
  }
  let penalty_before_id = null;
  try {
    penalty_before_id = fs.readFile( join( __dirname, 'penalty_before_id.txt'), 'utf8');
  }
  catch(err) {
    penalty_before_id='';
  }

  if(penalty_before_id != penalty.id_code) {
    
    fs.writeFile(join( __dirname, 'new_penalty.txt'), '1');

    fs.writeFile(join( __dirname, 'penalty_before_id.txt'), penalty.id_code);
    fs.writeFile(join( __dirname, 'penalty_team.txt'), penalty.team);
    fs.writeFile(join( __dirname, 'penalty_card.txt'), penalty.name.split("_")[1]);
    if (penalty.player.number != null)
      fs.writeFile(join( __dirname, 'penalty_playernumber.txt'), String(penalty.player.number));
    else
      fs.writeFile(join( __dirname, 'penalty_playernumber.txt'), '');

    if (penalty.player.name != null)
      fs.writeFile(join( __dirname, 'penalty_playername.txt'), penalty.player.name);
    else
      fs.writeFile(join( __dirname, 'penalty_playername.txt'), '');

    if (penalty.reason != null)
      fs.writeFile(join( __dirname, 'penalty_reason.txt'), penalty.reason);
    else
      fs.writeFile(join( __dirname, 'penalty_reason.txt'), '');
    log(chalk.bold('New penalty entry saved to penalty files "penalty_(...).txt".'));
  }
}

async function get_penalty_data(game) {
  if (game.events.length > 0) {
    for ( const element of game.events.slice().reverse()) {
      if (element.name.includes("penalty")) {
        return element;
      }
    }
  }
  return false;
}

/*****************/
/*** GAME TIME *** ==> latest after 30 seconds you realize if you aren't connected to the timekeeper anymore
/*****************/
function get_gametime_string( game_duration_ms ) {
  let minutes = parseInt( Math.floor( game_duration_ms / 1000 / 60 ) );
  let seconds = parseInt( Math.floor( game_duration_ms / 1000 - minutes * 60 ) );
  return minutes.toString().padStart( 2, '0' ) + ":" + seconds.toString().padStart( 2, '0' );
}
let last_paused_log = 0;
function log_paused_once_per_second( gametime_str ) {
  if( Date.now() - last_paused_log > 1000 ) {
    log( chalk.bold( 'Game is paused at ' ) + chalk.bold.blue( gametime_str ) );
    last_paused_log = Date.now();
  }
}
let logged_game_over = false;
function log_game_over_once( gametime_str ) {
  if( logged_game_over === false ) {
    log( chalk.bold( 'Game is over at ' ) + chalk.bold.blue( gametime_str ) );
    logged_game_over = true;
  }
}
async function gametime_loop( delay ) {
  let last_gametime_str = '';
  let last_connected;

  while( true ) {

    await sleep( delay );

    // error checks
    if( !game ) continue;

    try {
      // if no data available, wait for data to become available
      if( game.game_over == null ) {
        log( chalk.bold.red(`No game time data available. Did the timekeeper start the game?`) );
        await sleep( 1000 );
        continue;
      };

      const game_duration = ( game.gametime.running ) ? ( game.gametime.last_stop + ( get_timestamp_ms() - diff_to_server_ms ) - game.gametime.last_start ) : game.gametime.last_stop;
      const gametime_str = get_gametime_string( game_duration );

      if( game.game_over ) {
        log_game_over_once( gametime_str );
      }
      else if( gametime_str != last_gametime_str ) {
        logged_game_over = false;
        last_gametime_str = gametime_str;
        try {
          await fs.writeFile( join( __dirname, '../Output/Gametime.txt' ), gametime_str );
          await fs.writeFile( join( __dirname, '../Output/Gametime.csv' ), "Gametime\n"+gametime_str );
          log( chalk.bold( 'Gametime is ' ) + chalk.bold.blue( gametime_str ) + chalk( ' ==> saved to file "Gametime.txt and Gametime.csv".' ) );
        }
        catch ( err ) {
          log( err );
        }
      }
      else if( !game.gametime.running && game.game_over !== true ) {
        logged_game_over = false;
        log_paused_once_per_second( gametime_str );
      }

      if (game.overtime_setscore != null && !overtime_written) {
        await fs.writeFile( join( __dirname, '../Output/OvertimeSetscore.txt'), String(game.overtime_setscore));
        overtime_written = true
      }

      if( 'alive_timestamp' in game ) {
        let delta_from_last_alive_ms = ( get_timestamp_ms() - diff_to_server_ms ) - game.alive_timestamp * 1000;
        let connected = delta_from_last_alive_ms < 10000;
        if( connected !== last_connected ) {
          last_connected = connected;
          try {
            await fs.writeFile( join( __dirname, 'connected.txt' ), connected.toString() );
            if( connected) log( chalk.bold( 'The timekeeper is currently ' ) + chalk.bold.green( 'connected' ) + chalk( ' ==> saved to file "connected.txt".' ) );
            else log( chalk.bold( 'The timekeeper is currently ' ) + chalk.bold.red( 'not connected' ) + chalk( ' ==> saved to file "connected.txt".' ) );
          }
          catch( err ) {
            log( err );
          }
        }
      }
    }
    catch( err ) {
      log(err);
    }
  }
}
/*****************/
/*** EXECUTION ***/
/*****************/
diff_to_server_ms = await sync_to_server();
gametime_loop( delay );
game_id = await readGameID();
create_socket_connection( code, game_id );