/*
Write a function that computes the nth fibonacci number
*/

/*
Solution one:
Use a dynamic programming approach with memoization.
To print the fib sequence up to the nth term, run the function
and then print 0, 1 + the values of the memoizer object.
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
Solution two:
Without using recursion, return the sequence to the nth member.
To return only the last member and not the sequence, return
out[out.length-1]
*/

function fib_iterative(nth) {
    let n1 = 1, n2 =1, nextTerm;
    let out = [];
    for (let i = 1; i <= nth; i++) {
        out.push(n1);
        nextTerm = n1 + n2;
        n1 = n2;
        n2 = nextTerm;
    }
    return out;
}
console.log(fib_iterative(10));