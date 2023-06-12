#!/usr/bin/node

const args = process.argv;
const number = parseInt(args[2], 10);

if (args[2]) {
  if (number) {
    console.log(number);
  } else {
    console.log('Not a number');
  }
}
