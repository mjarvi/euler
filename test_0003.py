# -*- coding: utf-8 -*-
'''

 Problem 3
 Largest prime factor

 The prime factors of 13195 are 5, 7, 13 and 29.

 What is the largest prime factor of the number 600851475143 ?

'''
import math
import unittest

THE_BIG_NUMBER = 600851475143


def is_factor(value, factor):
    if value % factor == 0:
        return True
    return False


def is_prime(value):
    start_divider = 2
    end_divider = int(math.sqrt(value))
    for i in range(start_divider, end_divider):
        if value % i == 0:
            return False
    return True


class TestProblem3(unittest.TestCase):

    @unittest.skip('To be rewritten, kinda ugly now')
    def test(self):
        factor = 1
        while factor < THE_BIG_NUMBER:
            factor += 1
            if is_prime(factor):
                if is_factor(THE_BIG_NUMBER, factor):
                    print("found factor %d" % factor)
