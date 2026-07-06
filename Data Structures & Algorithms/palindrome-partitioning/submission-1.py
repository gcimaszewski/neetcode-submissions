class Solution:
    """
    Given a string s, split s into substrings where every substring is a palindrome.
    Return all possible lists of palindromic substrings.

    You may return the solution in any order.
    """
    
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        state = []
        
        # memoize palindrome checks for substrs of `s`
        # keys are index bounds ([start_idx, end_idx)); values are bool where True = is palindrome
        # initialize the memo table s.t. all single characters are palindromes
        memo = {(i, i+1): True for i in range(len(s))}

        def is_palindrome(str_):
            for i in range(len(str_)//2):
                if str_[i] != str_[len(str_) - 1 - i]:
                    return False
            return True

        def backtrack(i):
            if i >= len(s):
                palindromes.append(state[:])
                return
            
            # starting from `idx`: try to build all possible palindromes, 
            # up to (len(s) - idx ) // 2
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    continue
                is_palindrome = (i+1 >= j) or memo.get((i+1, j), False)
                memo[(i, j+1)] = is_palindrome
                if is_palindrome:
                # (i,j) are palindrome indices iff
                # s[i]==s[j] and (i+1,j-1) are also palindrome indices
              #  if (i, j+1) in memo and memo[(i, j+1)]:
                    state.append(s[i:j+1])
                    backtrack(j+1)
                    state.pop()
                # cand = s[idx:j+1]
                # # optimize the palindrome check by using a memo table
                # # because we repeatedly check whether certain substrs are palindromes or not
                # if is_palindrome(cand):
                #     state.append(cand)
                #     backtrack(j+1)
                #     state.pop()
        
        backtrack(0)
        return palindromes
