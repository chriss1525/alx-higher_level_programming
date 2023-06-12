#!/usr/bin/node

const args = process.argv;
const number = parseInt(args[2], 10);
let i;
let j;

if (args[2]) {
  if (number) {
    for (i = 0; i < number; i++) {
      let square = '';
      for (j = 0; j < number; j++) {
        square += 'X';
      }
      console.log(square);
    }
  } else {
    console.log('Missing size');
  }
}
