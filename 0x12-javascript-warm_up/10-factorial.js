#!/usr/bin/node

const args = process.argv;
const number = parseInt(args[2]);

function factorial (number) {
  if (number === 0 || isNaN(number)) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

console.log(factorial(number));
