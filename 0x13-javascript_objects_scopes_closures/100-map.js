#!/usr/bin/node
const { list } = require('./100-data');

const newList = list.map((item, i) => item * i);

console.log(list);
console.log(newList);
