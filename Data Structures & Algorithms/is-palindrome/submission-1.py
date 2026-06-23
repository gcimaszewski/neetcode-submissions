class Solution:
    def isPalindrome(self, s: str) -> bool:
        # approach:
        # set pointers on each end of the string (left, right)
        # compare if the character at left and right of the string is equal
        # (convert both to lowercase before comparison)
        # if either character is non-alphanumeric: 
        # then increment ONLY THAT pointer and continue to next iteration of the loop
        # (to do the comparison)
        # this has the effect of "stripping" all the non-alphanumeric chars as preprocessing
        left = 0
        right = len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
