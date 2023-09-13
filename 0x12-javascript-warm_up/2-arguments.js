#!/usr/bin/node
const myargment = process.argv.length;
if (myargment === 2){
  console.log('No argument');
} else if (myargment === 3){
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
