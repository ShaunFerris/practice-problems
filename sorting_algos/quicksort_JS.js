function quicksort(arr) {
  if (arr.length < 2) {
    return arr;
  }
  let pivot = arr[0];
  let lessers = arr.slice(1).filter((i) => i < pivot);
  let greaters = arr.slice(1).filter((i) => i > pivot);
  return quicksort(lessers).concat([pivot], quicksort(greaters));
}

const testArr = Array.from(
  { length: 20 },
  () => Math.floor(Math.random() * 100000) + 1
);
console.log(testArr);
console.log(quicksort(testArr));
