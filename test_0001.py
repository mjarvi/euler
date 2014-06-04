# -*- coding: utf-8 -*-
'''

 Problem 1 - Multiples of 3 and 5

 If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.

 Find the sum of all the multiples of 3 or 5 below 1000.

'''
import unittest

correct_answer = 233168


def is_multiple_of(multiplier, value):
    return value % multiplier == 0


def sum_of_natural_numbers_multiples_of_3_or_5(limit):
    return sum([value for value in range(limit)
               if is_multiple_of(3, value) or is_multiple_of(5, value)])


class problem1(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(sum_of_natural_numbers_multiples_of_3_or_5(1000), correct_answer)

    def test_example(self):
        self.assertEqual(sum_of_natural_numbers_multiples_of_3_or_5(10), 23)


if __name__ == '__main__':
    unittest.main()
