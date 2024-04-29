#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});callMeMoby('a', function () {
  console.log('C is fun');
});callMeMoby(0, function () {
  console.log('C is fun');
});
