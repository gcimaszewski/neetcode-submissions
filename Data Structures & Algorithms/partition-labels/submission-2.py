from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # split into as many substrings as possible
        # ideal case: all unique letters -> len(s) different substrings
        # else:
        # if a letter is repeated: it must be in the same substring as the first incidence of it
        # once we add a letter: expand the current substring to the last incidence of that letter
        counts = Counter(s)
        partitions = []
        part_len = 0
        window = 0
        maximum_index = 0
        last_index = {char: i for i, char in enumerate(s)}


        for idx, char in enumerate(s):
            part_len += 1
            # greedily extend our current partition's goalpost
            maximum_index = max(maximum_index, last_index[char])
            # if we reached the goalpost, we found a valid partition
            if idx == maximum_index:
                partitions.append(part_len)
                part_len = 0
                continue
            
            # when we add a new, unseen letter: need to add its count to window
            # if idx == first_seen_idx[char]:
            #     window += counts[char]
            # counts[char] -= 1
            # window -= 1
            # if window == 0:
            #     partitions.append(part_len)
            #     part_len = 0
            #     continue

        return partitions

# for "xyxxyzbzbbisl" ("xyxxy"):
# window = 3-1=2, part_len=1
# window = 2+2-1=3, part_len=2
# part_len=3, window=3-1=2
# part_len=4, window=2-1=1
# part_len=5, window=1-1=0

# for "abcabc":    
# len=1,window=2-1=1
# len=2, window=1+2-1 = 2
# len=3, window=2+2-1 = 3
# len=4, window=3-1=2
# len=5, window=2-1=1
# len=6, window=1-1=0
