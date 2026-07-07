class Solution:
    def numDecodings(self, s: str) -> int:
        
        char_num_encoding = {
            chr(ord('A') + i): f"{i+1}"
            for i in range(26)
        }
        encoding_inverted = {v:k for k,v in char_num_encoding.items()}
        # key: number string; value: the possible letters for it
        nd = {"": 1}
        right = 0
        # recurrence:
        # say we have numDecodings(s_0) stored.
        # s_1 = s_0 + "int"
        # numDecodings(s_1) = numDecodings(s_0)*numDecodings("int") + numDecodings(s_0[:-1])*numDecodings(s_0[-1]+"int")
        while right < len(s):
         #   to_decode = s[left:right+1]
            new_letter = s[right]
            s_0 = s[:right]
            last_letter = s_0[-1:]
            dc1 = nd.get(s_0)*len(encoding_inverted.get(new_letter, []))
            if last_letter:

                dc1 += nd.get(s_0[:-1])*len(encoding_inverted.get(last_letter+new_letter, []))
            nd[s_0 + new_letter] = dc1 
            right += 1
            # while (right - left + 1) > 2:
            #     left += 1
        
        return nd[s]
