from collections import Counter
from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(s1: str, s2: str) -> bool:

            if s1 == s2:
                return True

            if Counter(s1) != Counter(s2):
                return False
            
            n = len(s1)
            
            for i in range(1, n):

                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    return True

                if dfs(s1[:i], s2[n-i:]) and dfs(s1[i:], s2[:n-i]):
                    return True
            
            return False
        
        return dfs(s1, s2)