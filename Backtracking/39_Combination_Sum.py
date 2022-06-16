"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""

# Time Complexity -> O(2^N)
# Space Complexity -> O(N)

class Solution:
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates, target, [], 0)
        
        return self.result
    
    def dfs(self, candidates, target, record, iter_idx):
        current_sum = sum(record)
        if current_sum > target:
            return True
        elif current_sum == target:
            self.result.append(record[:])
        else:
            for i in range(iter_idx, len(candidates)):
                record.append(candidates[i])
                stop_flag = self.dfs(candidates, target, record, i)
                record.pop()
                
                if stop_flag: break
