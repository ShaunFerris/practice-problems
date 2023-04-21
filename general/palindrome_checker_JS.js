/*
Answers for the common basic coding interview question of writing a
function to detect wether or not an input string is palindromic.
*/

const notPali = "Hello"
const pali = "civic"

//First approach: use split and reverse methods then compare
function palindromeReverse(inputStr) {
    return inputStr === inputStr.split("").reverse().join("");
}

console.time("palindromeReverse")
console.log(palindromeReverse(pali))
console.timeEnd("palindromeReverse")
//Runs in about 3ms

//Second approach: reverse by iteration and then compare
function palindromeIterativeReverse(inputStr) {
    let reverseStr = "";
    for (let i = inputStr.length - 1; i >= 0; i--) {
        reverseStr += inputStr[i];
    }
    return inputStr === reverseStr
}

console.time("palindromeIterativeReverse")
console.log(palindromeIterativeReverse(pali))
console.timeEnd("palindromeIterativeReverse")
/*
Runs in about 0.1ms, significantly faster than first approach
but still slower than all my python solutions.
*/

/*
Third approach: Iterate to the middle comparing to the 
corresponding character from the end. The same as approach 2
in my python solutions
*/

function palindromeStartToEnd(inputStr) {
    for (let i = 0; i < Math.floor(inputStr.length / 2); i++) {
      if (inputStr[i] !== inputStr[inputStr.length - 1 - i]) {
        return false;
      }
    }
    return true;
  }

  console.time("palindromeStartToEnd")
  console.log(palindromeStartToEnd(pali))
  console.timeEnd("palindromeStartToEnd")
/*
Runs in about 0.09 - 0.1ms, significantly faster than first approach
but still slower than all my python solutions. About the same
as approach number 2 in this file, maybe slightly faster.
*/