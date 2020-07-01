#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function, find_anagrams(), which can be used to do the same
for an arbitrary list of strings.
"""

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = """DJJD2150, Corbin Creech, Mike A."""

import sys


def alphabetize(string):
    """Returns alphabetized version of the string."""
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
    # Creates a dictionary to put the words from the file called in the
    # words argument
    anagrams = {}
    # Loops through the words from the file called in the words argument
    for word in words:
        # if the alphabetized word is already in the dictionary as a key,
        # create it as a list and merge the list together with the
        # existing value list.  If it isn't already there, create it as
        # the new value list.  Then return the dictionary.
        if alphabetize(word) in anagrams.keys():
            anagrams[alphabetize(word)] += [word]
        else:
            anagrams[alphabetize(word)] = [word]
    return anagrams


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    with open(args[0]) as f:
        words = f.read().split()
    anagram_dict = find_anagrams(words)
    for k, v in anagram_dict.items():
        print(f"{k} : {v}")


if __name__ == "__main__":
    main(sys.argv[1:])
