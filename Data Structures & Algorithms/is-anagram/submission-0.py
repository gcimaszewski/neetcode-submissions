class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        
        for letter in t:
            if letter not in counts:
                return False
            else:
                counts[letter] -= 1

        return all([v == 0 for v in counts.values()])