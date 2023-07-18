/*
Bubble sort implementation. Examine each set of adjacent elements
from left to right, and switch their poistions if they are out
of order.
*/

const test = [13, 12, 145, 61, 2, 2, 4, 19, 75, 7];

function bubble(arr) {
  for (let i = 0; i < arr.length; i++) {
    let flag = true;
    for (let j = 1; j < arr.length; j++) {
      if (arr[j] < arr[j - 1]) {
        [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
        flag = false;
      }
    }
    if (flag === true) {
      break;
    }
  }
  return arr;
}

console.log(bubble(test));