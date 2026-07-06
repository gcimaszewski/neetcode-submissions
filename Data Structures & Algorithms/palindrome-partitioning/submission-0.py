class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        state = []

        def is_palindrome(str_):
            for i in range(len(str_)//2):
                if str_[i] != str_[len(str_) - 1 - i]:
                    return False
            return True

        def backtrack(idx):
            if idx >= len(s):
                palindromes.append(state[:])
                return
            
            # starting from `idx`: try to build all possible palindromes, 
            # up to (len(s) - idx ) // 2
            for j in range(idx, len(s)):
                cand = s[idx:j+1]
                if is_palindrome(cand):
                    state.append(cand)
                    backtrack(j+1)
                    state.pop()
        
        backtrack(0)
        return palindromes
