#!/usr/bin/node

const args = process.argv;
const number = parseInt(args[2], 10);

if (args[2]) {
  if (number) {
    console.log('My number: ', number);
  } else {
    console.log('Not a number');
  }
}
