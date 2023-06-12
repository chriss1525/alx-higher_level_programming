#!/usr/bin/node

const args = process.argv;
const i = 2;

if (args[i]) {
  console.log(args[i].concat(' is ', args[i + 1]));
}
