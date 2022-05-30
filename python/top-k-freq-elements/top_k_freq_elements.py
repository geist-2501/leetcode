from typing import List


# leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        word_bag = {}
        for num in nums:
            if num in word_bag:
                word_bag[num] += 1
            else:
                word_bag[num] = 1

        if k >= len(nums):
            return list(word_bag.keys())

        highest_freq_els = []
        for el, freq in word_bag.items():
            if len(highest_freq_els) < k:
                highest_freq_els.append(el)
            else:
                # If there is an element lower than the given, replace it.
                min_idx = min(range(len(highest_freq_els)), key=lambda i: word_bag[highest_freq_els[i]])
                if word_bag[highest_freq_els[min_idx]] < freq:
                    highest_freq_els[min_idx] = el

        return highest_freq_els


if __name__ == '__main__':
    s = Solution()
    # next_loc = s.get_next_loc([1, 2], {1: 2, 2: 4, 3: 3}, 3)
    # print(next_loc)
    # print(s.topKFrequent([1, 1, 1, 2, 2, 3], k=2))
    # print(s.topKFrequent([], k=3))
    # print(s.topKFrequent([1, 2, 3], k=3))
    # print(s.topKFrequent([1, 1, 1, 2, 2, 3], k=0))
    # print(s.topKFrequent([1, 1, 1, 1, 1, 1], k=2))
    print(s.topKFrequent([5, -3, 9, 1, 7, 7, 9, 10, 2, 2, 10, 10, 3, -1, 3, 7, -9, -1, 3, 3], k=3))
