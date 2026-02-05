"""
Author: Long Truong
Start: 5 Feb 2026
End: 5 Feb 2026
Problem title: Unique Paths II
Url: https://leetcode.com/problems/unique-paths-ii/description
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                    continue
                
                if i < 1:
                    up = 0
                else:
                    up = obstacleGrid[i-1][j]
                if j < 1:
                    left = 0
                else:
                    left = obstacleGrid[i][j-1]

                obstacleGrid[i][j] = up + left
        
        return obstacleGrid[-1][-1]
