#!/usr/bin/node
const prc = process.argv;

if (!isNaN(prc[2])) {
  funcy(prc);
} else {
  console.log('Missing number of occurrences');
}
function funcy (a) {
  let i;

  for (i = 0; i < a[2]; i++) {
    console.log('C is fun');
  }
}
