from typing import List


class Solution:
    def increasing_triplet(self, nums: List[int]) -> bool:
        a = 2**32
        b = 2**32
        for n in nums:
            if n <= a:
                a = n
            elif n <= b:
                b = n
            else:
                return True

        return False
