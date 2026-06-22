class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_counts = {}
        for char in s:
            letter_counts[char] = letter_counts.get(char, 0) + 1
        
        for char2 in t:
            if char2 not in letter_counts:
                return False
            allowance = letter_counts.get(char2, 0) - 1
            if allowance < 0:
                return False
            elif allowance == 0:
                del letter_counts[char2]
            else:
                letter_counts[char2] = allowance
        
        return letter_counts == {}