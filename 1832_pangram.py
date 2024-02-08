'''
Leetcode Problem No: 1832
Category: Easy
Source: Grokking the Coding Interview by Design Gurus
Problem Statement: "A pangram is a sentence where every letter
of the English alphabet appears at least once.
Given a string sentence containing English letters (lower or upper-case),
return true if sentence is a pangram, or false otherwise.
Note: The given sentence might contain other characters like digits or spaces,
your solution should handle these too."
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set()

        for s in sentence.lower():
            if s.isalpha() and s not in alphabets:
                alphabets.add(s)
        
        return len(alphabets) == 26

sol = Solution()
print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(sol.checkIfPangram("This is not a pangram"))
