#!/usr/bin/node
const prc = process.argv;
if (!isNaN(prc[2])) {
  let i;

  for (i = 0; i < prc[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
