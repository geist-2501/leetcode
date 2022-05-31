from typing import List


# leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
