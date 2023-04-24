/*
Write a function to flatten the contents of a provided array,
which may or may not contain other nested arrays.

The key to this problem is to find a way to measure the depth of
provided multi-dimensional arrays, and then you can simply use the
built-in JS method Array.prototype.flat() with the depth parameter.
*/

/*
Recursively measure the depth of an array. When an element is not an
array return 0. When it is, return 1 + a map of the arrays elements onto
this function, thus you will return 1 for every array inside another array.
*/
function getDepth(arr) {
    return Array.isArray(arr) ?
        1 + Math.max(0, ...arr.map(getDepth)) :
        0;
}

function steamRoll(arr) {
    const depth = getDepth(arr);
    return arr.flat(depth)
}

let testArr = [1,2,[3,4,[5,6],7,[8,[9,91]],10],11,12];

console.log(steamRoll(testArr));

/*
Or do it all in one go without using the flat() builtin by
using recursion to traverse the list directly. This is the 
equivalent of the python solution to this problem is this directory.
*/
function iterSteamroll(arr) {
    let out = [];
    for (let i of arr) {
        if (Array.isArray(i)) {
            out = out.concat(iterSteamroll(i));
        } else out.push(i);
    }
    return out;
}

console.log(iterSteamroll(testArr));