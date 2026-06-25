class Solution:
    """
    You are given a string s consisting of only uppercase english characters and an integer k.
    You can choose up to k characters of the string and replace them with any other uppercase English character.

    After performing at most k replacements, 
    return the length of the longest substring which contains only one distinct character.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        # goal: find longest repeating char substring with maximum k edits
        # strategy: decompose s into its constituent repeated char substrings
        # then find the ideal insertion points for the k edits

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
            most_common_letter = max(char_counts.keys(), key=char_counts.get)
            window_size = right - left + 1
            # how many characters in this window are NOT the most common one?
            num_edits = window_size - char_counts[most_common_letter]
            print(f'left: {left}  right: {right} window size: {window_size}')
            print(f'char counts here: {char_counts}')
            print(f'most frequent character: {most_common_letter}  num edits: {num_edits}')                
            if num_edits > k:
                char_counts[s[left]] -= 1 
                if char_counts[s[left]] == 0:
                    del char_counts[s[left]]
                left += 1
            
            longest_substr_len = max(longest_substr_len, right - left + 1)
            right += 1
            print(f'longest length: {longest_substr_len}')
        return longest_substr_len