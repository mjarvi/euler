# -*- coding: utf-8 -*-
'''

 Problem 4

 Largest palindrome product

 A palindromic number reads the same both ways. The largest
 palindrome made from the product of two 2-digit numbers is 9009 = 91x99.

 Find the largest palindrome made from the product of two 3-digit numbers.

'''
import unittest

correct_answer = 906609


def is_palindrome(value):
    numbers_in_value = list(str(value))
    for index in range(len(numbers_in_value) / 2):
        lv = numbers_in_value[index]
        rv = numbers_in_value[len(numbers_in_value) - 1 - index]
        if lv != rv:
            return False
    return True


class problem4(unittest.TestCase):

    def test_solution(self):
        palindromes = []
        for a_value in range(100, 999):
            for b_value in range(100, 999):
                value = a_value * b_value
                if is_palindrome(value):
                    palindromes.append(value)

        highest_value = sorted(palindromes)[-1]
        self.assertEqual(highest_value, correct_answer)

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome(123), False)
        self.assertEqual(is_palindrome(1234321), True)


if __name__ == '__main__':
    unittest.main()
