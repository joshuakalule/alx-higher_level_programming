#!/usr/bin/node
// Computes the number of tasks completed by user id
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(`Status: ${response.statusCode}`);
    return;
  }
  const tasksCompleted = {};
  for (const task of JSON.parse(body)) {
    if (!(task.completed)) {
      continue;
    }
    if (task.userId in tasksCompleted) {
      tasksCompleted[task.userId]++;
    } else {
      tasksCompleted[task.userId] = 1;
    }
  }
  console.log(tasksCompleted);
});
