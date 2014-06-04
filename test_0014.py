# -*- coding: utf-8 -*-
'''

 Problem 14 - Longest Collatz sequence

 The following iterative sequence is defined for the set of positive integers:

 n → n/2 (n is even)
 n → 3n + 1 (n is odd)

 Using the rule above and starting with 13, we generate the following sequence:

 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 It can be seen that this sequence (starting at 13 and finishing at 1) contains
 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
 that all starting numbers finish at 1.

 Which starting number, under one million, produces the longest chain?

 NOTE: Once the chain starts the terms are allowed to go above one million.

'''
import unittest

correct_answer = 837799


def get_collatz_sequence(starting_from):
    sequence = [starting_from]
    n = starting_from
    while n != 1:
        n = (3 * n) + 1 if n % 2 else n / 2
        sequence.append(n)
    return sequence


def get_collatz_sequences(from_value, to_value):
    for starting_from in range(from_value, to_value):
        yield get_collatz_sequence(starting_from)


class problem14(unittest.TestCase):

    def test_solution(self):
        lengths_of_sequences = [len(sequence) for sequence in get_collatz_sequences(1, 999999)]
        longest_length = max(lengths_of_sequences)
        self.assertEqual(lengths_of_sequences.index(longest_length) + 1,
                         correct_answer)

    def test_get_collatz_sequences(self):
        self.assertEqual(get_collatz_sequence(13),
                         [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])


if __name__ == '__main__':
    unittest.main()
