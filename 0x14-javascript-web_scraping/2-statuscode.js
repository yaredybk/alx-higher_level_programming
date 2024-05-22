#!/usr/bin/node
// web scraping

const req = require('request');
req.get(process.argv[2]).on('response', (response)=>
	console.log(`code: ${response.statusCode}`);
});
