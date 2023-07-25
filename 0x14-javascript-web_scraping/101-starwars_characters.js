#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];
const log = console.log;

request(url + movieId, function (error, response, body) {
  if (error) {
    log(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request(character, function (error, response, body) {
        if (error) {
          log(error);
        } else {
          log(JSON.parse(body).name);
        }
      });
    });
  }
});
