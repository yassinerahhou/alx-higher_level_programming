#!/usr/bin/node
const myargment = process.argv;

if (myargment[2] === undefined && myargment[3] === undefined) {
  console.log('undefined is undefined');
} else {
  console.log(myargment[2] + ' is ' + myargment[3]);
}
