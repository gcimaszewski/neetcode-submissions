class Solution:

    def encode(self, strs: List[str]) -> str:
        # the encoding needs to give the decoding function
        # some way to determine the start/ending indexes of each str
        # note that integers are part of the allowed ASCII character set, 
        # so we can't rely on them exactly 
        # maximum length of string: 200
        # idea: prefix the string with the length (padded to 3 digits)

        def _get_padded_len(num):
            if 0 <= num < 10:
                return "00" + str(num)
            elif 10 <= num < 100:
                return "0" + str(num)
            else:
                return str(num)
        
        encoding_bldr = []
        for word in strs:
            len_prfx = _get_padded_len(len(word))
            encoding_bldr.append((len_prfx + word))
        
        return "".join(encoding_bldr)

    def decode(self, s: str) -> List[str]:

        read_idx = 0
        words = []
        while read_idx < len(s):
            idx_end_of_prfx = read_idx + 3
            word_len = int(s[read_idx: idx_end_of_prfx])
            word = s[idx_end_of_prfx: idx_end_of_prfx + word_len]
            words.append(word)
            read_idx += 3 + word_len
        return words
