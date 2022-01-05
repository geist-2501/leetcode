# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/827/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * (n + 1)
        right = [0] * (n + 1)

        left[0] = 1
        right[n] = 1
        for i in range(1, n + 1):
            left[i] = left[i-1] * nums[i - 1]

        for i in range(n - 1, -1, -1):
            right[i] = right[i+1] * nums[i]

        ans = [0] * n
        for i in range(n):
            ans[i] = left[i] * right[i+1]

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
