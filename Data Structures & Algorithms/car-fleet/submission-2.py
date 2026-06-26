class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # the car at max position determines the minimum time to reach target
        stack = list(sorted(zip(position, speed)))
        leader_pos, leader_v = stack.pop()
       # t_arrive = -((target - leader_pos) // - leader_v)
        t_arrive = (target - leader_pos)/leader_v
        num_fleets = 1
        while len(stack) > 0:
            pos, v = stack.pop()
            # check if this car will catch up to the previous car before the target
            t = -((target - pos)// -v)
            t = (target-pos)/v
            print(f'{pos}, v={v} t = {t}. compared to {t_arrive}')
            if t <= t_arrive:
                # include it in the fleet
                continue
            else:
                num_fleets += 1
                t_arrive  = t
        return num_fleets