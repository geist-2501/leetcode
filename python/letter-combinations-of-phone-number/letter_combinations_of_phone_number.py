from typing import List

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
# 2 - abc
# 3 - def
# 4 - ghi
# 5 - jkl
# 6 - mno
# 7 - pqrs
# 8 - tuv
# 9 - wxyz

class Solution:
    choices = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        result = self.dfs(digits, "")

        if result == [""]:
            return []

        return result

    def dfs(self, digits: str, perm: str) -> List[str]:
        if digits == "":
            return [perm]

        digit = digits[0]
        digits_remaining = digits[1:]
        options = self.choices[digit]

        combos = []
        for opt in options:
            combos.extend(self.dfs(digits_remaining, perm + opt))

        return combos
