class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS from `src` to `dst` 
        # because price != num hops, we cannot use BFS

        dist = [float('inf') for _ in range(n)]
        paths = [[] for _ in range(n)]

        dist[src] = 0

        for nstops in range(k+1):
            frozen = dist[:]
            frozen_paths = [_[:] for _ in paths]
            for idx, flt in enumerate(flights):
                (start_arpt, end_arpt, price) = flt
                alt = frozen[start_arpt] + price
                if dist[end_arpt] > alt:
                    dist[end_arpt] = alt
                    paths[end_arpt] = frozen_paths[start_arpt] + [idx]
        
        # now we have the list of the airport order in predecessor
        # predecessor stores the index of the ticket to do that next hop
        # print the series of actual flights taken
        for idx in paths[dst]:
            print(flights[idx])
        return dist[dst] if dist[dst] != float('inf') else -1
        

