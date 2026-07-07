class Solution:
    def countSubstrings(self, s: str) -> int:
        # approach#;
        # keep a table of index ranges [i, j) and their palindrome status
        # try all palindromes for each length 1..len(s)
        p = {}
        # base case: all single letters are palindromes
        num_palindromes = 0
        for i in range(len(s)):
            p[(i, i+1)] = True
            num_palindromes += 1
            # useful for looping: set the empty strings as palindromes as well
            p[(i,i)] = True
        
        # a string s[i:j+1] is a palindrome if:
        # 1. s[i] = s[j] and
        # 2. s[i+1:j] is also a palindrome

        # iteration: for substring of len i, last starting index in s is len(s) - i
        for palindrome_len in range(2, len(s) + 1):
            for i in range(len(s) - palindrome_len + 1):
                j = i + palindrome_len
                is_palindrome = (s[i] == s[j-1]) and p[(i+1,j-1)]
                num_palindromes += is_palindrome
                p[(i, j)] = is_palindrome
        
        return num_palindromes
