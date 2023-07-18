/*
Write a function that returns the first repeated character in a given string.
Eg: in the string "YABCFDFAB" A is the first repeated character, because it is 
the earliest appearing character that is repeated. If no characters repeat, return None.
*/

const TEST_INPUT = "YABCFDFAB";
const TEST_INPUT_2 = "ABCDEFGHIJJK";

function slow_solution(input_str) {
  for (let index = 0; index < input_str.length; index++) {
    const c = input_str[index];
    for (let j = index + 1; j < input_str.length; j++) {
      const c2 = input_str[j];
      if (c === c2) {
        return c;
      }
    }
  }
  return null;
}

console.time("slow_solution");
console.log(better_solution(TEST_INPUT_2));
console.timeEnd("slow_solution");

function better_solution(input_str) {
  const counts = {};
  for (const c of input_str) {
    if (c in counts) {
      return c;
    } else {
      counts[c] = 1;
    }
  }
  return null;
}

console.time("better_solution");
console.log(better_solution(TEST_INPUT_2));
console.timeEnd("better_solution");