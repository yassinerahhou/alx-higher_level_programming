#!/usr/bin/node

// const fs = require('fs');
const request = require('request');
const url = process.argv[2];

// Request URL
// let url = 'https://jsonplaceholder.typicode.com/todos/1';

request(url, (error, response) => {
  // Printing the error if occurred
  if (error) console.log(error);

  // Printing status code
  console.log('code:', response.statusCode);

  // Printing body
  // console.log(body);
});
