#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
const log = console.log;

request(url, function (error, response, body) {
  if (error) {
    log(error);
  } else {
    const json = JSON.parse(body);
    log(json.title);
  }
});
