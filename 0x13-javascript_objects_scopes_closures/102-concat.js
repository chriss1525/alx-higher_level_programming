#!/usr/bin/node

const fs = require('fs');

const [file1, file2, file3] = process.argv.slice(2);

const data1 = fs.readFileSync(file1, 'utf8');
const data2 = fs.readFileSync(file2, 'utf8');

const data = data1 + data2;

fs.writeFileSync(file3, data);
