/*
Write a function that computes the nth fibonacci number
Use a dynamic programming approach with memoization.
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
/*
To print the fib sequence up to the nth term, run the function
and then print the values of the memoizer object.
*/
Object.values(memoizer).forEach(val => console.log(val));