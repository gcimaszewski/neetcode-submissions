class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # need to get to the last gast station
        # need gas_in_tank + gas[last] - cost[last] >= 0
        gas_in_tank = 0
        roadlen = len(gas)
        # initial check
        if sum(cost) > sum(gas):
            return -1

        station_idx = 0
        while station_idx < len(gas):
            gas_in_tank = 0 
            for j in range(roadlen):
                next_station = (station_idx+j)%roadlen
                gas_in_tank += (gas[next_station] - cost[next_station])
                if gas_in_tank < 0:
                    break
            if gas_in_tank >= 0:
                return station_idx
            station_idx += j + 1
        return -1