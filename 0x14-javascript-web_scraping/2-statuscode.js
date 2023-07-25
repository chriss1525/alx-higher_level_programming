#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const log = console.log;
request(url, function (error, response) {
  if (error) {
    log(error);
  } else {
    log('code: ' + response.statusCode);
  }
});
