"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""

# Time Complexity -> O(N!)
# Space Complexity -> O(N)

class Solution:
    def __init__(self):
        self.result = []
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.dfs(nums, [], [True for _ in range(len(nums))])
        
        return self.result
    
    def dfs(self, nums, record, flags):
        print(record, flags)
        if len(record) == len(nums):
            self.result.append(record[:])
        else:
            for i in range(len(nums)):
                if i >= 1 and (flags[i - 1]) and nums[i] == nums[i - 1]:
                    continue
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
