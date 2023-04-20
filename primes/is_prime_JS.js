/*
Implementation of the sieve of Erastothenes, a classical 
method for determining if a number is prime or not.
*/

/*
Solution one:
Basic seive, with the 6k +/- 1 optimization, meaning that 
all primes greater than 3 are of the form 6k ± 1, where k 
is any integer greater than 0. Other more complex 
implementations are much faster for larger n.
*/
function isPrime(n) {
    if (n <= 3) return n > 1;
    if (n % 2 === 0 || n % 3 === 0) return false;
    let limit = Math.floor(n**0.5);

    for (let i = 5; i < limit; i += 6) {
        if (n % i === 0 || n % (i + 2) === 0) {
            return false;
        }
    }
    return true;
}

for (let i = 1; i <= 50; i++) {
    if (isPrime(i)) console.log(i); 
}