from typing import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            bag = self.get_word_bag(word)
            if bag in anagrams:
                anagrams[bag].append(word)
            else:
                anagrams[bag] = [word]

        return list(anagrams.values())

    def get_word_bag(self, word: str) -> FrozenSet[str]:
        bag = {}
        for letter in word:
            if letter in bag:
                bag[letter] = bag[letter] + 1
            else:
                bag[letter] = 1

        return frozenset(bag.items())
