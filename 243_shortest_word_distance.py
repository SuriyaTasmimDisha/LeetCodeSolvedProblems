'''
Leetcode Problem No: 243
Category: Easy
Source: Grokking the Coding Interview by Design Gurus
Problem Statement: "Given an array of strings words and two different
strings that already exist in the array word1 and word2, return the 
shortest distance between these two words in the list."
'''


class Solution:
  def shortestDistance(self, words, word1, word2):
    distance = position1 = position2 = float('inf')
    i = 0
     
    while i<len(words):
        if words[i] == word1:
            position1 = i
        if words[i] == word2:
            position2 = i
        if abs(position1-position2) != float('inf') and abs(position1-position2) < distance:
            distance = abs(position1-position2)
        i += 1
    return distance
        
    

sol = Solution()
print(sol.shortestDistance(words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], word1 = "fox", word2 = "dog"))
print(sol.shortestDistance(words = ["a", "c", "d", "b", "a"], word1 = "a", word2 = "b"))
print(sol.shortestDistance(words = ["a", "b", "c", "d", "e"], word1 = "a", word2 = "e"))