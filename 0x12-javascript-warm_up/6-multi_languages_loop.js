#!/usr/bin/node
const myarray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
printo(myarray);
function printo (a) {
  for (let i = 0; i < a.length; i++) {
    console.log(a[i]);
  }
}
