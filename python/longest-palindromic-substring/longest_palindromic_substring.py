class Solution:
    def longest_palindrome(self, s: str) -> str:
        longest = s[0]  # s or sss etc
        il = 0
        ir = 0
        while il < len(s) and ir < len(s):
            left = il
            right = ir
            while left >= 0 and right < len(s) and s[left] == s[right]:
                pal = s[left:(right + 1)]
                if len(pal) > len(longest):
                    longest = pal
                left -= 1
                right += 1

            if il == ir:
                ir += 1
            else:
                il += 1

        return longest


if __name__ == '__main__':
    s = Solution()
    print(s.longest_palindrome("babad"))
    print(s.longest_palindrome("cbbd"))
    print(s.longest_palindrome("cbb"))
