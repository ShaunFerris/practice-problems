/*
Write a function that computes the fibonnaci number at a given index i
along the fibonacci sequence. Use a dynamic programming approach with memoization.
*/

const memoizer = {};

function fib(i) {
    const key = '' + i;
    if (key in memoizer) {
        return memoizer[key];
    }
    if (i === 0) {
        return 0;
    } else if (i === 1) {
        return 1;
    }

    const result = fib(i - 1) + fib(i - 2);
    memoizer[key] = result;
    return result;
}

console.log(fib(10))