import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def _dist_to_origin(x_coord, y_coord):
            return (x_coord**2 + y_coord**2)**0.5

        # we want a max heap of length k
        # that holds the k closest points
        k_closest = []
        for p in points:
            dist = -1 * _dist_to_origin(*p) # negate to make python minheap into maxheap
            if len(k_closest) < k:
                heapq.heappush(k_closest, (dist, p))
            else:
                top_k_max_dist, _ = k_closest[0]
              #  heapreplace(k_closest, (-dist, p))
                if dist > top_k_max_dist:
                    _ = heapq.heapreplace(k_closest, (dist, p))
                #   heapq.heappush((dist, p))
        return [_[1] for _ in k_closest]