class Solution:
    """
    You are given a string s consisting of only uppercase english characters and an integer k.
    You can choose up to k characters of the string and replace them with any other uppercase English character.

    After performing at most k replacements, 
    return the length of the longest substring which contains only one distinct character.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        # hint: find the most common character across the sliding window, not the whole string
        longest_substr_len = 0
        char_counts = {}
        while right < len(s):
            new_letter = s[right]
            
            # workflow:
            # add s[right] to the window
            # if window invalid: move left forward; remove s[left]
            # update answer
            char_counts[new_letter] = char_counts.get(new_letter, 0) + 1
            # this is O(number of distinct characters in the current window), or O(26) (English alphabet)
            max_count = max(char_counts.values())
            # how many characters in this window are NOT the most common one?
            if (right - left + 1) - max_count > k:
                char_counts[s[left]] -= 1 
                if char_counts[s[left]] == 0:
                    del char_counts[s[left]]
                left += 1
            
            longest_substr_len = max(longest_substr_len, right - left + 1)
            right += 1
        return longest_substr_len