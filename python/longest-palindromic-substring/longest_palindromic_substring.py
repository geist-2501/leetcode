class Solution:
    def longest_palindrome(self, s: str) -> str:
        # Check odd palindromes.
        longest = s[0]  # s or sss etc
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                pal = s[left:(right + 1)]
                if len(pal) > len(longest):
                    longest = pal
                left -= 1
                right += 1

        for i in range(len(s) - 1):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                pal = s[left:(right + 1)]
                if len(pal) > len(longest):
                    longest = pal
                left -= 1
                right += 1

        return longest


if __name__ == '__main__':
    s = Solution()
    print(s.longest_palindrome("babad"))
