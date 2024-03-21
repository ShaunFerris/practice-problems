function selectSort(arr) {
  let output = [];
  while (arr.length > 0) {
    let smallIdx = arr.indexOf(Math.min(...arr));
    output.push(arr.splice(smallIdx, 1)[0]);
  }
  return output;
}

// Example usage:
let testArr = Array.from(
  { length: 15 },
  () => Math.floor(Math.random() * 10000) + 1
);
console.log(selectSort(testArr));
