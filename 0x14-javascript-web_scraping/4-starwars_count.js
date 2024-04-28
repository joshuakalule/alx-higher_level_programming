#!/usr/bin/node
/**
 * Prints the number of movies where the character
 * “Wedge Antilles” is present
 */
const request = require('request');

const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (resp.statusCode !== 200) {
    console.log(`Status: ${resp.statusCode}`);
  } else {
    const charId = '/18/';
    const movies = JSON.parse(body).results;
    const count = movies.filter(movie => {
      for (const char of movie.characters) {
        if (char.endsWith(charId)) return true;
      }
      return false;
    });
    console.log(count.length);
  }
});
