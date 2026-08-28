from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start_index, current_combo, remaining_target):

            if remaining_target == 0:
                res.append(list(current_combo))
                return
            

            if remaining_target < 0:
                return
            

            for i in range(start_index, len(candidates)):
                current_combo.append(candidates[i])

                backtrack(i, current_combo, remaining_target - candidates[i])

                current_combo.pop()
                
        backtrack(0, [], target)
        return res