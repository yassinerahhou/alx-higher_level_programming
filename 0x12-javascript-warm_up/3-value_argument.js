#!/usr/bin/node
const myargment = process.argv;
if (myargment[2] === undefined) {
  console.log('No argument');
} else {
  console.log(myargment[2]);
}
