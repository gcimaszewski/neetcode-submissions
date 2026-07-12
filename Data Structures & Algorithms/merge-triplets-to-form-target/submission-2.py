class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # for a candidate triple i, where i_0,i_1,i_2 each <=t_0,t_1,t_2:
        # if we AND it with another triplet j and then any of res_0,res_1,res_2 > target:
        # then triplet j is "bad" and it's not part of the solution
        # any triplet that has any of the three values higher than target is unusable
        triplets.sort()

        result = [1, 1, 1]
        for i, triple in enumerate(triplets):
            (a, b, c) = triple
            if any(triple[i] > target[i] for i in range(3)):
                continue
            result[0] = max(result[0], a)
            result[1] = max(result[1], b)
            result[2] = max(result[2], c)
        return all(result[i] == target[i] for i in range(3))