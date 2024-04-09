#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  let i = 0;
  while (args[i] === args[i + 1]) i++;
  console.log(args[i + 1]);
}
