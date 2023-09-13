#!/usr/bin/node
const prc = process.argv;

if (!isNaN(prc[2])) {
  funcy(prc);
} else {
  console.log('Missing size');
}
function funcy (a) {
  let i;
  let y;
  let op = '';
  for (i = 0; i < a[2]; i++) {
    for (y = 0; y < a[2]; y++) {
      op += 'X';
    }

    console.log(op);
    op = '';
  }
}
