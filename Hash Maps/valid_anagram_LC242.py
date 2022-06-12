"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false"""

#Time: O(n)
#Space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = Counter(s)
        second = Counter(t)
        
        for letter in first:
            if first[letter] != second[letter]:
                return False
        
        for letter in second:
            if first[letter] != second[letter]:
                return False
        
        return True