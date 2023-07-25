#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const log = console.log;

request(url, function (error, response, body) {
  if (error) {
    log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) {
          log(error);
        } else {
          log(JSON.parse(body).name);
        }
      });
    }
  }
});
