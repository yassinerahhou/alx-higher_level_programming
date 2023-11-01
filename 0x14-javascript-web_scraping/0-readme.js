#!/usr/bin/node
// const filep = process.argv[2];
const fs = require('fs');
const file = fs.readFileSync(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
console.log(file);
