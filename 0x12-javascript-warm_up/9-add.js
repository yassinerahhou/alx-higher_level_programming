#!/usr/bin/node
const prc = process.argv;

if (!isNaN(prc[2]) && !isNaN(prc[3])) {
  add(prc[2], prc[3]);
} else {
  console.log('NaN');
}
function add (a, b) {
  console.log(Number(a) + Number(b));
}
