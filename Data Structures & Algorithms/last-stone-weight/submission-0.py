import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # approach: use a maxheap
        # to do the stone smashing: get the top 2 elements on the maxheap
        # do the smashing operation
        # add the smashing result (if applicable) back to the heap
        # continue until len(maxheap) == 1

        heap_of_stones = [-1*s for s in stones]
        heapq.heapify(heap_of_stones)
        while len(heap_of_stones) > 1:
            biggest_stone = heapq.heappop(heap_of_stones)
            next_biggest = heapq.heappop(heap_of_stones)
            if biggest_stone == next_biggest:
                continue
            new_stone = -1 * abs(biggest_stone - next_biggest)
            heapq.heappush(heap_of_stones, new_stone)
        

        if len(heap_of_stones) == 0:
            return 0
        else:
            return -1*heap_of_stones[0]
