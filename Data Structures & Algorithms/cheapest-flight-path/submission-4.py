class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS from `src` to `dst` 
        # because price != num hops, we cannot use BFS

        dist = [float('inf') for _ in range(n)]
        predecessor = [None for _ in range(n)]

        dist[src] = 0

        for nstops in range(k+1):
            frozen = dist[:]
            for idx, flt in enumerate(flights):
                (start_arpt, end_arpt, price) = flt
                alt = frozen[start_arpt] + price
                if dist[end_arpt] > alt:
                    dist[end_arpt] = alt
                    predecessor[end_arpt] = idx
        
        # now we have the list of the airport order in predecessor
        # predecessor stores the index of the ticket to do that next hop
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
        if predecessor[dst] ==  None:
            return -1
        
        # traverse through predecessors to get the actual itinerary
        flight = flights[predecessor[dst]]
        cheapest_price = flight[2]
        while True:
            flight = flights[predecessor[flight[0]]]
            cheapest_price += flight[2]
            if flight[0] == src:
                break
        return cheapest_price
        

