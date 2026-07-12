class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # for a candidate triple i, where i_0,i_1,i_2 each <=t_0,t_1,t_2:
        # if we AND it with another triplet j and then any of res_0,res_1,res_2 > target:
        # then triplet j is "bad" and it's not part of the solution
        # any triplet that has any of the three values higher than target is unusable
        # greedy structure: performing the operation with any triplet that is under target is harmless

        result = [0, 0, 0]
        matched_indices = set()
        for t in triplets:
           # (a, b, c) = t
            if any(t[i] > target[i] for i in range(3)):
                continue
            for i in range(3):
                if t[i] == target[i]:
                    matched_indices.add(i)
            
            if len(matched_indices) == 3:
                return True
            # result[0] = max(result[0], a)
            # result[1] = max(result[1], b)
            # result[2] = max(result[2], c)
        return False
        #return all(result[i] == target[i] for i in range(3))