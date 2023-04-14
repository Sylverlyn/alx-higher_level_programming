#!/usr/bin/node

const myArgs = process.argv;
if (myArgs.length <= 2) {
  console.log('No argument');
} else {
  console.log(myArgs[2]);
}
