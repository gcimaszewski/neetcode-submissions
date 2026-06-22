class Solution:

    def getAnagramId(self, word):
        counts = {}
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1
        id_builder = []
        for idx in range(ord('a'), ord('z') + 1):
            letter = chr(idx)
            count_in_word = counts.get(letter, 0)
            if count_in_word > 0:
                id_builder.append(letter + str(count_in_word))
        return "".join(id_builder)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        # map a particular anagram to the index of the group
        anagram_to_group = {}
        for word in strs:
            # the canonical anagram string is the word sorted
            #anagram_id = ''.join(sorted(word))
            # improved from O(n*log(n)) -> O(n)
            anagram_id = self.getAnagramId(word)
            if anagram_id in anagram_to_group:
                groups[anagram_to_group[anagram_id]].append(word)
            else:
                anagram_to_group[anagram_id] = len(groups)
                groups.append([word])
        return groups

