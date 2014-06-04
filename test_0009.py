# -*- coding: utf-8 -*-
'''

 Problem 9 - Special Pythagorean triplet

 A Pythagorean triplet is a set of three natural
 numbers, a < b < c, for which,

    a^2 + b^2 = c^2

 For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

 There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 Find the product abc.

'''
import unittest

correct_answer = (200, 375, 425)


def is_pythagorean_triplet(a, b, c):
    return (a ** 2) + (b ** 2) == (c ** 2)


def find_pythagorean_triplet(sum):
    for a in range(1, sum):
        for b in range(1, sum):
            c = sum - a - b
            if is_pythagorean_triplet(a, b, c):
                return a, b, c
    return 0, 0, 0


class problem09(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(find_pythagorean_triplet(1000), correct_answer)

    def test_example(self):
        self.assertEqual(find_pythagorean_triplet(12), (3, 4, 5))


if __name__ == '__main__':
    unittest.main()
