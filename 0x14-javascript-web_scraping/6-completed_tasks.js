#!/usr/bin/node

const request = require('request'); // Import 'request' module
const URL = process.argv[2]; // Assign command-line arg
// Send a request to the URL
request(URL, function (err, response, body) {
	if (err) {
		console.log(err); // Print error message if an error occurred
	} else if (response.statusCode === 200) {
		const complete = {};
		const tasks = JSON.parse(body);
		for (const a in tasks) {
			const task = tasks[a];
			if (task.complete === true) {
				if (complete[task.userId] === undefined) {
					complete[task.userId] = 1;
				} else {
					complete[task.userId]++;
				}
			}
		}
		console.log(complete);
	} else {
		console.log('An error occured. Status code: ' + response.statusCode);
	}
});
