'''
Leetcode Problem No: 242
Category: Easy
Source: Grokking the Coding Interview by Design Gurus
Problem Statement: "Given two strings s and t, return true if
t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters exactly once."
'''
from collections import Counter

class Solution:
  def isAnagram(self, s, t):
    return Counter(s) == Counter(t)

sol = Solution()
print(sol.isAnagram(s = "listen", t = "silent"))
print(sol.isAnagram(s = "rat", t = "car"))
print(sol.isAnagram(s = "hello", t = "world"))