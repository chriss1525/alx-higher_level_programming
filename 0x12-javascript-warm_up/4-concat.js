#!/usr/bin/node

const args = process.argv;
let i = 2;
if (args[i]) {
  console.log(args[i].concat(' is ', args[i + 1]));
}
else{
  console.log('undefined is undefined');
}
