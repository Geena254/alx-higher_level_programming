#!/usr/bin/node

const request = require('request'); // Import 'request' module
const fs = require('fs'); // Import filesystem module
const URL = process.argv[2];
const file_name = process.argv[3];

// Send a request to the URL
request(URL, (error, response, body) => {
	if (error) {
		console.log(error); // Print error message if an error occurred
	} else {
		fs.writeFile(file_name, body, encoding='utf-8', (error) => {
			if (error) {
				console.log(error); // Print error message if an error occurred
			}
		});
	}
});
