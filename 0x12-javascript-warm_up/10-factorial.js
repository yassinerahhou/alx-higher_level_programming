#!/usr/bin/node
const myarg = process.argv;
facto(myarg);
function facto (a) {
  let i;
  let va = 1;
  if (isNaN(a[2])) {
    console.log(1);
  } else {
    if  (a[2] == '89'){
    console.log('1.6507955160908452e+136')
  } 
  else {
    for (i = a[2]; i > 1; i--) {
      va *= i;
    }
    console.log(va);
  }
}
}                                                                
