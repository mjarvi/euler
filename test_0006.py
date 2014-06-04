# -*- coding: utf-8 -*-
'''

 Problem 6 - Sum square difference

 The sum of the squares of the first ten natural numbers is,
 1^2 + 2^2 + ... + 10^2 = 385

 The square of the sum of the first ten natural numbers is,
 (1 + 2 + ... + 10)^2 = 552 = 3025

 Hence the difference between the sum of the squares of
 the first ten natural numbers and the square of the sum
 is 3025 - 385 = 2640.

 Find the difference between the sum of the squares of the first
 one hundred natural numbers and the square of the sum.

'''
import unittest

correct_answer = 25164150


def get_sum_of_squares_of_range(values):
    return sum([x ** 2 for x in range(0, values + 1)])


def get_square_of_sum_of_range(values):
    return sum(range(values + 1)) ** 2


class problem6(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(
            get_square_of_sum_of_range(100) - get_sum_of_squares_of_range(100),
            correct_answer)

    def test_sum_of_squares_of_the_first_ten(self):
        self.assertEqual(get_sum_of_squares_of_range(10), 385)

    def test_square_of_the_sum_of_first_ten(self):
        self.assertEqual(get_square_of_sum_of_range(10), 3025)


if __name__ == '__main__':
    unittest.main()
