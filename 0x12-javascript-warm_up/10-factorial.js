#!/usr/bin/node
const myarg = process.argv;
facto(myarg);

function facto (a) {
  let i;
  let va = 1;
  if (isNaN(a[2])) {
    console.log(1);
  } else {
    for (i = a[2]; i > 1; i--) {
      va *= i;
    }
    console.log(va);
  }
}
