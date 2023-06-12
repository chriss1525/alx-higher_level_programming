#!/usr/bin/node
const args = process.argv;

function second (args) {
  if (args.length <= 3) {
    return (0);
  }

  if (!args[2]) {
    return (0);
  }

  let biggest = 0;
  let second = 0;
  for (let i = 2; i < args.length; i++) {
    if (parseInt(args[i]) > biggest) {
      second = biggest;
      biggest = parseInt(args[i]);
    } else if (parseInt(args[i]) > second) {
      second = parseInt(args[i]);
    }
  }
  return (second);
}

console.log(second(args));
