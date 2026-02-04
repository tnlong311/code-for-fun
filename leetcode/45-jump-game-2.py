"""
Author: Long Truong
Start: 4 Feb 2026
End: 4 Feb 2026
Problem title: 45. Jump Game II
Url: https://leetcode.com/problems/jump-game-ii/description/
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curren = 0
        step = 0
        n = len(nums)

        while (curren < n-1):
            k = nums[curren]
            mx = k
            temp = curren
            for i in range(1, k+1):
                if (curren+i >= n-1):
                    temp = curren+i
                    break
    
                f = nums[curren+i]+curren+i
                if (f >= mx):
                    temp = curren+i
                    mx = f

            curren = temp
            step += 1

        return step
        
