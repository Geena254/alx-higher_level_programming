#!/usr/bin/node

const request = require('request'); // Import 'request' module
const URL = process.argv[2];
const characterID = '18';
let cnt = 0;

// Send a GET request to the URL
request.get(URL, (error, response, body) => {
	if (error) {
		console.log(error); // Print error message if an error occurred
	} else {
		const info = JSON.parse(body);
		info.results.forEach((film) => {
			film.characters.forEach((character) => {
				if (character.includes(characterID)) {
					cnt += 1; // Counts how many times charcterID is found in tthe charcters
				}
			});
		});
		console.log(cnt); // Prints how many charcterID 18 were found
	}
});
