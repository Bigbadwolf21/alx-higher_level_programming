#!/usr/bin/node
const countValue = process.argv.length;
console.log(countValue === 2 ? 'No argument' : countValue === 3 ? 'Argument found' : 'Arguments found');
