#!/usr/bin/node
const myargment = process.argv;
if (myargment.length === 2) {
  console.log('No argument');
} else if (myargment.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
