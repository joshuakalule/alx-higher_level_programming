#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(`code: ${response.statusCode}`);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (const characterURL of characters) {
    request(characterURL, (err2, response2, body2) => {
      if (err2) {
        console.log(err2);
        return;
      }
      if (response2.statusCode !== 200) {
        console.log(`code: ${response2.statusCode}`);
        return;
      }
      console.log(JSON.parse(body2).name);
    });
  }
});
