#!/usr/bin/node

const fs = require('fs'); // Import filesystem module
const file_name = process.argv[2]; // Assign command-line arg

fs.readFile(file_name, encoding='utf-8', (err, fileContent) => {
	if(err) {
		console.log(err); // Print error message if an error occurred
	} else {
		console.log(fileContent); // Print file content on success
	}
});
