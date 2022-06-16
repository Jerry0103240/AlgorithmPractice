"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""

# Time Complexity -> O(2^N)
# Space Complexity -> O(N)

class Solution:
    def __init__(self):
        self.result = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates, target, [], 0)
        
        return self.result
    
    def dfs(self, candidates, target, record, iter_idx):
        cur_sum = sum(record)
        if cur_sum > target:
            return True
        elif cur_sum == target:
            self.result.append(record[:])
        else:
            for i in range(iter_idx, len(candidates)):
                if i > iter_idx and candidates[i] == candidates[i - 1]:
                    continue
                record.append(candidates[i])
                stop_flag = self.dfs(candidates, target, record, i + 1)
                record.pop()
                
                if stop_flag: break
