#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');

const movieId = process.argv[2];
const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

fetchData(baseUrl)
  .then((movie) => {
    return Promise.all(movie.characters.map(char => fetchData(char)));
  })
  .then((characters) => {
    characters.forEach(char => {
      console.log(char.name);
    });
  })
  .catch((error) => {
    console.log(error);
  });
