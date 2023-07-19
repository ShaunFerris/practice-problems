/*
Create a function that takes two inputs and returns true if they are anagrams
or false if they are not.
*/

//Solution one, blind attempt at solving the problem
function isAnagram(w1, w2) {
  if (w1.length !== w2.length) {
    return false;
  } else {
    let letList1 = [...w1];
    let letList2 = [...w2];
    let memo = [];

    for (let i = 0; i < letList1.length; i++) {
      if (!memo.includes(letList1[i])) {
        memo.push(letList1[i]);
      } else {
        continue;
      }
      if (
        letList2.filter((e) => e === letList1[i]).length !=
        letList1.filter((e) => e === letList1[i]).length
      ) {
        return false;
      }
    }
    return true;
  }
}

let w1 = "gardenn";
let w2 = "dangerr";
console.time("isAnagram");
console.log(isAnagram(w1, w2));
console.timeEnd("isAnagram");

//Solution 2, using objects to store letter counts. Significantly faster.
function dictAnagram(w1, w2) {
  if (w1.length !== w2.length) {
    return false;
  } else {
    let w1Dict = {};
    let w2Dict = {};

    for (let c of w1) {
      w1Dict[c] = w1Dict[c] ? w1Dict[c] + 1 : 1;
    }
    for (let c of w2) {
      w2Dict[c] = w2Dict[c] ? w2Dict[c] + 1 : 1;
    }

    const w1Keys = Object.keys(w1Dict);

    for (let i = 0; i < w1Keys.length; i++) {
      const key = w1Keys[i];
      if (!w2Dict.hasOwnProperty(key)) {
        return false;
      }
      if (w1Dict[key] !== w2Dict[key]) {
        return false;
      }
    }
    return true;
  }
}

console.time("dictAnagram");
console.log(dictAnagram(w1, w2));
console.timeEnd("dictAnagram");
