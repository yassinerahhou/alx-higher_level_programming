#!/usr/bin/node
const myargment = process.argv;
if (myargment[2] === undefined) {
  console.log( myargment[2]+' is '+myargment[3]);

}else if (myargment.length === 3) {
  console.log( myargment[2]+' is '+myargment[3]); 
}else {
  console.log(myargment[2]+' is '+myargment[3]);
}
