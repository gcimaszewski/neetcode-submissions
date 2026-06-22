class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        ret = []
        for word in strs:
            letter_freqs = self.get_letters_map(word)
            has_group = False
            for group_idx, group_freqs in groups.items():
                if group_freqs == letter_freqs:
                    ret[group_idx].append(word)
                    has_group = True
                    break
            if not has_group:
                ret.append([word])
                groups[len(ret) - 1] = letter_freqs

        return ret

    
    def get_letters_map(self, word):
        freqs = {}
        for letter in word:
            if letter not in freqs:
                freqs[letter] = 0
            freqs[letter] += 1
        return freqs