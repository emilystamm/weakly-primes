# weakly-primes
Fast python algorithm for determining if a prime is weakly base b

A prime number p is a weakly prime in base b if when written in its base b expansion p = a_nb^n + ... + a_1b + a_0, if you switch any a_i for any other integer in the set k in {0,...,b-1}\{a_i}, then the resulting number p' = a_nb^n + ... + kb^i + ... + a_1b + a_0 is composite. Tau proved that for any base b,  a positive propotions of primes are weakly prime base b. See https://en.wikipedia.org/wiki/Weakly_prime_number 

In the weakly prime tests the author has seen, the prime is first converted to it's base b expansion, often in an array, and then a matrix is formed of all the possible p' - this matrix is of shape  b-1 by floor(log p base b) + 1. This involves many conversions back and forth between integers and integers in some base representation as an array, which is computationally intensive. 

This algorithm uses simple operations (addition, multiplication, exponentiation, and modular congruences) to determine if a number is weakly prime, making it much more efficient. Note one should use an efficient prime test for the isprime function - we use the sympy isprime.  

  
