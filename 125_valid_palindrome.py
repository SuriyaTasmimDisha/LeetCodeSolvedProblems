'''
Leetcode Problem No: 1832
Category: Easy
Source: Grokking the Coding Interview by Design Gurus
Problem Statement: "A phrase is a palindrome if, after converting all
uppercase letters into lowercase letters and removing all non-alphanumeric
characters, it reads the same forward and backward. Alphanumeric characters
include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
    
                
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal, Panama!"))
print(sol.isPalindrome("Was it a car or a cat I saw?"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome("0P"))