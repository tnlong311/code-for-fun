"""
Author: Long Truong
Start: 6 Feb 2026
End: 6 Feb 2026
Problem title: Longest Palindrome
Url: https://leetcode.com/problems/longest-palindrome/
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}

        for i in range(len(s)):
            char = s[i]
            if char in mp:
                mp[char]+=1
            else:
                mp[char] = 1
        
        count = 0
        is_odd = False
        for key in mp:
            if mp[key] % 2 == 1:
                is_odd = True

            count += (mp[key] // 2) * 2
        
        if is_odd:
            count += 1

        return count
