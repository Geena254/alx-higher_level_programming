#!/usr/bin/node

const request = require('request'); // Import 'request' module
const movieID = process.argv[2];
const url = 'https://swapi.dev/api/films/${movieID}/';

// Send a GET request to the URL
request.get(url, (error, response, body) => {
	if (error) {
		console.log(error); // Print error message if an error occurred
		return;
	}
	const info = JSON.parse(body);
	const characters = info.characters;
	for (const character of characters) {
		request(character, (error, response, body) => {
			if (error) {
				console.log(error); // Print error message if an error occurred
				return;
			}
			const characterInfo = JSON.parse(body);
			console.log(characterInfo.name);
		});
	}
});
