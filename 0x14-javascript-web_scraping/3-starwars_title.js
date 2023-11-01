#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const options = { json: true };

request(url + id, options, (error, res) => {
  if (error) {
    return console.log(error);
  }

  if (!error && res.statusCode === 200) {
    // do something with JSON, using the 'body' variable
    console.log(res.body.title);
  }
});
