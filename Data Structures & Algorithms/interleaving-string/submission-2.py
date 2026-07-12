class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if not len(s3) == len(s1) + len(s2):
            return False
        memo = {}
        def backtrack(i, j):
            k = i + j
            state = (i,j)
            if state in memo:
                return memo[state]
            if k == len(s3):
                return i==len(s1) and j==len(s2)
            if (i < len(s1) and s3[k] == s1[i] and
                backtrack(i+1,j)
            ):
                memo[state] = True
                return memo[state]
            if (
                j < len(s2) and
                s3[k] == s2[j] and 
                backtrack(i, j+1)
            ):
                memo[state]= True
                return memo[state]
            memo[state] = False
            return memo[state]

        return backtrack(0, 0)


            