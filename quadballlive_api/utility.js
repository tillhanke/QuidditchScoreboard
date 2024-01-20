import fetch from 'node-fetch';
import chalk from 'chalk';
import { dirname } from 'path';
import { fileURLToPath } from 'url';
import _ from 'lodash';
import { host } from './env.js';
import { DateTime } from 'luxon';
import fs from 'fs/promises';

const __dirname = dirname( fileURLToPath( import.meta.url ) );

/**********************/
/*** HELP FUNCTIONS ***/
/**********************/
export const log = function() { let args = Array.from(arguments); args.unshift( get_current_time_string() ); console.log.apply(console, args); } // prepend timestamp to console.log
export function get_current_time_string() { const currentTime = DateTime.local(); const formattedTime = currentTime.toFormat('yyyy-MM-dd @ HH:mm:ss'); return formattedTime; }
export const sleep = ( ms ) => new Promise( resolve => setTimeout( resolve, ms ) );
export const get_timestamp_ms = () => Date.now();
export async function sync_to_server() {
  let start = get_timestamp_ms();
  log( chalk.bold( 'Fetching from "' + host + '/api/open/time' + '"' ) );
  let server_time = await fetch( host + '/api/open/time' ).then( ( resp ) => resp.json() );
  let stop = get_timestamp_ms();
  let diff = parseInt( ( start + stop ) / 2 - server_time.timestamp );
  log( chalk.bold( 'Time difference between local and server time is ') + chalk.bold.blue( diff + 'ms' ) + chalk.bold( '. ' + ( diff > 0 ? 'The server lags behind.' : 'Your local machine lags behind.' ) ) );
  return diff;
} /* if result is positive, local time is ahead and server time lags behind */
export async function read_game_id() {
  let game_id;
  // try to read from file game_id.txt first
  try {
    game_id = await fs.readFile( __dirname + '/game_id.txt', 'utf8' );
    log( chalk.bold( 'Public Game Code from file (delete file if you want to connect to other game): ' ) + chalk.bold.green( game_id ) );
    return game_id;
  }
  catch (e) {
    log( chalk.bold( 'No game_id.txt file found. Trying from user input.' ) );
  }
}
export const hex_to_rgb = (hex) => {
  // Remove the '#' symbol if it's present
  hex = hex.replace('#', '');

  // Parse the hex values for r, g, and b components
  const r = parseInt(hex.substring(0, 2), 16);
  const g = parseInt(hex.substring(2, 4), 16);
  const b = parseInt(hex.substring(4, 6), 16);

  return { r, g, b };
}