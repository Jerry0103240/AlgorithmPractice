"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

# Time Complexity -> O(N!)
# Space Complexity -> O(N)

class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.dfs(nums, [], [True for _ in range(len(nums))])
        return self.result

    
    def dfs(self, nums, record, flags):
        if len(record) == len(nums):
            self.result.append(record[:])
        else:
            for i in range(len(nums)):
                if flags[i]:
                    self.lock(flags, i)
                    record.append(nums[i])
                    self.dfs(nums, record, flags)
                    record.pop()
                    self.unlock(flags, i)

    def lock(self, flags, idx):
        flags[idx] = False
    
    def unlock(self, flags, idx):
        flags[idx] = True
