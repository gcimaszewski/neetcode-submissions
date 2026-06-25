class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if a permutation of s1 exists as a substring of s2
        # order matters! we can't merely do letter counts
        # the letters can be scrambled but they must be contiguous
        # use a sliding window
        # compare the letter counts in the sliding window to s1 letter counts
        # iterate through the whole s2
        left = 0
        perm_letter_counts = {}
        window = {}
        for char in s1:
            perm_letter_counts[char] = perm_letter_counts.get(char, 0) + 1
        for right in range(len(s2)):
            new_letter = s2[right]
            window[new_letter] = window.get(new_letter, 0) + 1
            window_size = right - left + 1
            if window_size == len(s1):
                # check if the substring is a permutation of s1
                # if yes, return true
                # if not: move left forward and update the window
                if perm_letter_counts == window:
                    return True
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
        return False
