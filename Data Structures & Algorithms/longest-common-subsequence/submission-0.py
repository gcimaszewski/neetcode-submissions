class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        c = [[0 for i in range(len(text1)+1)] for j in range(len(text2) +1) ]

        for i in range(1, len(text2)+1):
            for j in range(1, len(text1) + 1):
                if text2[i-1] == text1[j-1]:
                    c[i][j] = 1 + c[i-1][j-1]
                elif c[i][j-1] > c[i-1][j]:
                    c[i][j] = c[i][j-1]
                else:
                    c[i][j] = c[i-1][j]
        
        return c[len(text2)][len(text1)]
