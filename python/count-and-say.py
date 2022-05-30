# leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/4153/

class Solution:
    def countAndSay(self, n: int) -> str:
        prev_res = "1"
        for i in range(n - 1):
            prev_res = self.count_and_say(int(prev_res))

        return prev_res

    def count_and_say(self, n: int):

        n_as_chars = str(n)
        chosen_char = n_as_chars[0]
        num_chars = 0
        out_str = ""
        for char in n_as_chars:
            if char == chosen_char:
                num_chars += 1
            else:
                out_str += str(num_chars) + str(chosen_char)
                num_chars = 1
                chosen_char = char

        out_str += str(num_chars) + str(chosen_char)

        return out_str


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(4))
