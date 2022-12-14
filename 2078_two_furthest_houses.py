"""
There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
"""

class Solution:
    def maxDistance(self, A):
        res = 0
        for i, x in enumerate(A):
            if x != A[0]:
                res = max(res, i)
            if x != A[-1]:
                res = max(res, len(A) - 1 - i)
        return res