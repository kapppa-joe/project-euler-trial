# Project Euler trial

A repo to store my attempts in solving project Euler problems with a TDD and FP approach.

## Description

I started this repo for some practice on TDD & functional programming in Python.

For each problem, rather than just computing the required numerical answer, my approach in this repo would be to create a general solution func that can accept different parameters.

Also, for practice purpose, here I try to implement my custom classes/function to solve the mathematical problems, rather than using the std lib provided.

Some of the custom classes/functions I have implemented:

- A generator of fibonacci numbers

- A generator of prime number from 1 to n

- A function to produce all primes below n, using the Sieve of Eratosthenes algorithm

- A custom BigNumber class implemented with singly linked lists, which supports addition / subtraction / multiplication / factorial

- A quicksort function

Test for each solution function and util function are included as well.

(I use Pytest as the testing framework here)
