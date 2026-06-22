class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups_map = {}
        ret = []
        for word in strs:
            letter_freqs = self.get_letters_map(word)
            if letter_freqs in groups_map:
                ret[groups_map[letter_freqs]].append(word)
            else:
                ret.append([word])
                groups_map[letter_freqs] = len(ret) - 1
            # has_group = False
            # for group_idx, group_freqs in groups.items():
            #     if group_freqs == letter_freqs:
            #         ret[group_idx].append(word)
            #         has_group = True
            #         break
            # if not has_group:
            #     ret.append([word])
            #     groups[len(ret) - 1] = letter_freqs
        return ret

    
    def get_letters_map(self, word):
        hist = [0 for _ in range(26)]
        for letter in word:
            letter_idx = ord(letter) - ord('a')
            hist[letter_idx] += 1
        return ';'.join([str(_) for _ in hist])