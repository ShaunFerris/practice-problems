/*
Write a function to find the lowest common multiple for
all numbers in a range between the two numbers provided in
an array.
*/

const testArray = [1, 5];

function lcm(arr) {
   const [min, max] = arr.sort((a, b) => a - b);
   const range = Array(max - min + 1)
      .fill(0)
      .map((value, index) => index + min);
   //multiply the whole range to find the upper limit
   let limit = range.reduce((product, current) => product * current);
   for (let multiple = max; multiple <= limit; multiple += max) {
      if (range.every((value) => multiple % value === 0)) {
         return multiple;
      }
   }
}

console.log(lcm(testArray));