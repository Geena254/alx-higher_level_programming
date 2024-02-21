#!/usr/bin/node

const request = require('request'); // Import 'request' module
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/:movieID';

// Send a GET request to the URL
request.get(url, (error, response, body) => {
	if (error) {
		console.log(error); // Print error message if an error occurred
	} else {
		const info = JSON.parse(body);
		console.log(info.title);
	}
});
