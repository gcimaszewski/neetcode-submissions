# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ptr = 0
        states = []
        while ptr < len(pairs):
            idx = self.find_right_idx(pairs, 0, ptr, pairs[ptr])
         #   print(f'at ptr {ptr}, found the right idx as {idx} for {pairs[ptr].key}')
            self.insert_at(pairs, pairs[ptr], idx, ptr)
          #  print(f'now:')
          #  for j in pairs:
          #      print(f'\t{j.key}:{j.value}')
            states.append(pairs.copy())
            ptr += 1
        return states
    

    def find_right_idx(self, ls, start, stop, new_val):
        the_idx = stop
        for i in range(start, stop):
            if new_val.key < ls[i].key:
                the_idx = i
                break
        return the_idx


    def insert_at(self, ls, new_val, new_idx, bound):

        for idx in range(bound, new_idx, -1):
            # shift over the old elements
            ls[idx] = ls[idx - 1]
        ls[new_idx] = new_val


    def swap(self, ls, i, j):
        tmp = ls[i]
        ls[i] = ls[j]
        ls[j] = tmp