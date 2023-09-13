#!/usr/bin/node
let myn = process.argv;
if(isNaN(myn[2])){
  console.log("Not a number");
} else {
  console.log('My number: ' + (myn[2]));
}
