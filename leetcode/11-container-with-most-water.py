"""
Author: Long Truong
Date: 6 Jan 2025
Problem title: 11. Container With Most Water
Url: https://leetcode.com/problems/container-with-most-water
"""

# Brute force
# class Solution:
#   def maxArea(self, height: List[int]) -> int:
#     re = 0
#     n = len(height)
#     for i in range(n-1):
#       for j in range(i+1,n):
#         a = height[i]
#         if height[i] > height[j]:
#           a = height[j]
#         area = (j-i)*a

#         if area > re:
#           re = area

#     return re

class Solution:
  def maxArea(self, height: List[int]) -> int:
    pass