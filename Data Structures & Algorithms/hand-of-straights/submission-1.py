from collections import defaultdict
from queue import PriorityQueue
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = defaultdict(int)
        pq = PriorityQueue()
        for card in hand:
            cnt[card] += 1
            pq.put(card)
        while not pq.empty():
            while cnt[pq.queue[0]] == 0:
                pq.get()
                if pq.empty():
                    return True
            card = pq.queue[0]
            for _ in range(groupSize):
                if cnt[card] == 0:
                    return False
                cnt[card] -= 1
                card += 1
        return True
            