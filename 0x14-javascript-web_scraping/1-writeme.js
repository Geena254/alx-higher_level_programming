#!/usr/bin/node

const fs = require('fs'); // Import filesystem module
const file_name = process.argv[2];  // As 3rd command-line arg
const fileContent = process.argv[3];  // As 4th command-line arg

fs.writeFile(file_name, fileContent, encoding='utf-8', (error) => {
	if (error) {
		console.log(error); // Print error message if an error occurred
	}
});
