class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if a permutation of s1 exists as a substring of s2
        # order doesn't matter, but the matching letters must form a contiguous substring
        # the letters can be scrambled but they must be contiguous
        # use a sliding window
        # compare the letter counts in the sliding window to s1 letter counts
        # iterate through the whole s2
        if len(s1) > len(s2):
            return False
        left = 0
        target = {}
        window = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1
        for right, char in enumerate(s2):
            window[char] = window.get(char, 0) + 1
            window_size = right - left + 1
            if window_size == len(s1):
                # check if the substring is a permutation of s1
                # if yes, return true
                # if not: move left forward and update the window
                if target == window:
                    return True
                left_char = s2[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1
        return False
