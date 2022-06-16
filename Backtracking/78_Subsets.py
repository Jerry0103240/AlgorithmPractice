"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

# Time Complexity -> O(N * 2^N)
# Space Complexity -> O(N)

class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, [], 0)
        return self.result

    def dfs(self, nums, record, iter_idx):
        self.result.append(record[:])
        for i in range(iter_idx, len(nums)):
            record.append(nums[i])
            self.dfs(nums, record, i + 1)
            record.pop()
