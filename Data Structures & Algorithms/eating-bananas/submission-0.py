from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # goal: eat all piles within h hours
        # len(piles) is a floor on the number of hours to finish eating everything
        # approach: take the smallest pile
        # 1 <= k <= max(piles)
        # given a rate of k:
        # all piles <= k take 1 hour, 
        # piles > k take ceiling(pile/k) hours

        largest_pile = max(piles)
        good_k = []
        stack_of_bigger = []
        cost_fixed = 0
        for p in piles:
            if p == 1:
                cost_fixed += 1
            else:
                stack_of_bigger.append(p)
        # maybe keep a stack with everything greater than the current k?
        # invariant: caneat(i, h) = False for any i <= left
        # caneat(j, h) = True for any j>= right 
        # minimum value of k will be equal to right at the end of the loop 
        left = 0
        right = largest_pile + 1
        while left + 1 < right:
            k = left + (right - left)//2
            hrs_to_eat = 0
            for p in piles:
                hrs_to_eat += ceil(p/k)
            if hrs_to_eat > h:
                left = k
            else:
                right = k
        return right


        # for k in range(1, largest_pile + 1):
        #     cost = 0
        #     # get the cost 
        #     for p in piles:
        #         cost += ceil(p/k)
        #         if p > k:
        #             stack_of_bigger.append(k)
        #     print(f'{k} {cost}')
        #     if cost <= h:
        #         print(f'appending {k} because cost is {cost} which is lteq {h}')
        #         good_k.append(k)
        # print(good_k)
        # return good_k[0] if good_k else None
