#!/usr/bin/node
function factorial(n) {
  if (!n || n < 2) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);

console.log(factorial(num));
