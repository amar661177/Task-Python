

class Solution:

    @staticmethod
    def longest_palindromic(text: str) -> str:
         max_len = 0
         max_word = ""
         for first in range(len(text)):
            for second in range(first + 1, len(text) + 1):
                word = text[first:second]
                if (word == word[::-1]):
                    if max_len < len(word):
                        max_len = len(word)
                        max_word = word
         return max_word



print("Example 1 : " , Solution().longest_palindromic("babad"))

print("Example 2 :" , Solution().longest_palindromic("cbbd"))

print("Example 3 : " , Solution().longest_palindromic("a"))

print("Example 4 :" , Solution().longest_palindromic("ac"))



