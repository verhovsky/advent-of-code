#!/usr/bin/env python3
import string

with open("5.txt") as f:
    polymer = f.read().strip()


def is_compliment(a, b):
    # return true if a and b are the same letter in different cases
    # True for aA Aa
    # False for AA aa
    return (a.lower() == b or a.upper() == b) and b != a


def react(polymer):
    polymer = list(polymer).copy()
    while True:
        for index, first in enumerate(polymer[:-1]):
            second = polymer[index + 1]
            if is_compliment(first, second):
                polymer.pop(index)
                polymer.pop(index)
                break
        else:
            return polymer


# print(len(react(polymer)))

print(min(len(react(polymer.replace(letter, "").replace(letter.upper(), ""))) for letter in string.ascii_lowercase))
