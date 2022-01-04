# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/
from typing import List


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

    def get_word_bag(self, word: str) -> str:
        return ''.join(sorted(word))
