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
        for i in range(len(gas)):
            gas_in_tank += (gas[i] - cost[i])
            if gas_in_tank < 0:
                station_idx = i+1
                gas_in_tank = 0
        return station_idx