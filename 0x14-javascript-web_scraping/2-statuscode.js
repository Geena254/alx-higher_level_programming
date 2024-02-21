#!/usr/bin/node

const request = require('request'); // Import 'request' module
const URL = process.argv[2];
// Send a GET request to the URL
request.get(URL, (err, response) => {
	if (err) {
		console.log(err); // Print error message if an error occurred
	} else {
		console.log('code: ${response.statusCode}'); // Print the status code on success
	}
});
