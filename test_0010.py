# -*- coding: utf-8 -*-
'''

 Problem 10 - Summation of primes

 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

 Find the sum of all the primes below two million.

'''
import unittest

correct_answer = 142913828922


def is_prime(n):
    ''' Thanks to http://www.daniweb.com/software-development/python/code/216880/check-if-a-number-is-a-prime-number-python'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def sum_primes(highest):
    result = 0
    number = 0
    while number < highest:
        if is_prime(number):
            result += number
        number += 1
    return result


class problem10(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(sum_primes(2000000), correct_answer)

    def test_example(self):
        self.assertEqual(sum_primes(10), 2 + 3 + 5 + 7)


if __name__ == '__main__':
    unittest.main()
