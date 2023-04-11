/*
Create a function that takes two inputs and returns true if they are anagrams
or false if they are not.
*/

//Solution one, blind attempt at solving the problem
function isAnagram(w1, w2) {
    let letList1 = [...w1];
    let letList2 = [...w2];
    if (letList1.length !== letList2.length) {
      return false;
    } else {
      for (let i = 0; i < letList1.length; i++) {
        if (!letList2.includes(letList1[i])) {
          return false;
        }
      }
      return true;
    }
  }
  
  let w1 = 'garden';
  let w2 = 'danger';
  console.time("isAnagram")
  console.log(isAnagram(w1, w2)); // Output: true
  console.timeEnd("isAnagram")