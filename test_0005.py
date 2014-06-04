# -*- coding: utf-8 -*-
'''

 Problem 5 - Smallest multiple

 2520 is the smallest number that can be divided by each
 of the numbers from 1 to 10 without any remainder.

 What is the smallest positive number that is evenly
 divisible by all of the numbers from 1 to 20?

'''
import unittest

correct_answer = 232792560


def is_factor(number, factor):
    return float(number) % factor == 0


def is_all_dividable(candidate, range_of_factors):
    for factor in range_of_factors:
        if not is_factor(candidate, factor):
            return False
    return True


def find_smallest_number_dividable_with_all_below(limit):
    candidate = 1
    range_of_factors = range(1, limit)
    while True:
        if is_all_dividable(candidate, range_of_factors):
            return candidate
        candidate += 1


class problem5(unittest.TestCase):

    @unittest.SkipTest
    def test_solution(self):
        self.assertEqual(find_smallest_number_dividable_with_all_below(21), correct_answer)

    def test_example(self):
        self.assertEqual(find_smallest_number_dividable_with_all_below(10), 2520)


if __name__ == '__main__':
    unittest.main()
