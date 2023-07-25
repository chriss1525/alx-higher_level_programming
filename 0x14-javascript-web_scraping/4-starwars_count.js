#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const log = console.log;

request(url, function (error, response, body) {
  if (error) {
    log(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    log(count);
  }
});
