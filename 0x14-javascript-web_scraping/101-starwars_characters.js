#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];
const log = console.log;

function printCharactersInOrder (characters, index) {
  if (index >= characters.length) {
    return;
  }

  const character = characters[index];
  request(character, function (error, response, body) {
    if (error) {
      log(error);
    } else {
      const name = JSON.parse(body).name;
      log(name);
    }

    // Recursively call the function to print the next character in order
    printCharactersInOrder(characters, index + 1);
  });
}

request(url + movieId, function (error, response, body) {
  if (error) {
    log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharactersInOrder(characters, 0);
  }
});
