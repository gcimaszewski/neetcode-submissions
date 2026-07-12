from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # greedy: sort `hand` and pick up the smallest card
        # if number is unique, add it to the most recent group with len < groupSize
        # if this card - last card > 1, return false
        # else, make new group
        # why the greedy choice works:
        # suppose that we have a group g where len(g) < groupSize (still being built)
        # if g contains cards i..j-1, and the next member of the card is NOT card j
        # 

        if len(hand) % groupSize != 0:
            return False
        card_counts = Counter(hand)
        card_values = list(card_counts.keys())
        heapq.heapify(card_values)
        
        groups_created = 0
        while card_values:
            smallest_card = heapq.heappop(card_values)
            if card_counts[smallest_card] < 1:
                continue
            for i in range(groupSize):
                
                card = smallest_card + i
                print(f'{smallest_card} testing {card} {card_counts}')
                if card_counts.get(card, 0) < 1:
                    return False
                card_counts[card] -= 1
            if card_counts[smallest_card] > 0:
                heapq.heappush(card_values, smallest_card)
            groups_created += 1
        return True

