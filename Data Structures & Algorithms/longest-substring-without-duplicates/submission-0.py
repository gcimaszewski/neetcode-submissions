class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # approach: 
        # use a sliding window with two pointers
        # initialize the pointers to the first character of the string
        # expand the window rightward until the uniqueness constraint is broken
        # update the longest length accordingly
        # when non-unique character found: move window left until constraint restored
        # then continue expanding right
        # continue expanding and shrinking window until right index reaches end of the string
        left, right = 0, 0
        longest_len = 0
        seen_letters = set()
        while right < len(s):
            if s[right] in seen_letters:
                # update
                while s[right] in seen_letters:
                    seen_letters.remove(s[left])
                    left += 1
                continue
            else:
                seen_letters.add(s[right])
                longest_len = max(longest_len, len(seen_letters))
                right += 1
        return longest_len
