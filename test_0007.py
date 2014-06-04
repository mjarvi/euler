# -*- coding: utf-8 -*-
'''

 Problem 7 - 10001st prime

 By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
 we can see that the 6th prime is 13.

 What is the 10 001st prime number?

'''
import unittest

correct_answer = 104743


# cheating a bit here, for this part thanks to:
# http://www.daniweb.com/software-development/python/code/216880/check-if-a-number-is-a-prime-number-python
def is_prime(n):
    '''check if integer n is a prime'''
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


def get_nth_prime_number(n):
    prime_index = 0
    candidate = 1
    while prime_index != n:
        candidate += 1
        if is_prime(candidate):
            prime_index += 1
    return candidate


class problem7(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(get_nth_prime_number(10001), correct_answer)

    def test_example(self):
        self.assertEqual(get_nth_prime_number(1), 2)
        self.assertEqual(get_nth_prime_number(3), 5)
        self.assertEqual(get_nth_prime_number(6), 13)


if __name__ == '__main__':
    unittest.main()
