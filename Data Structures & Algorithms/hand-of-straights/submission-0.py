from collections import defaultdict
from queue import PriorityQueue
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = defaultdict(int)
        pq = PriorityQueue()
        for card in hand:
            cnt[card] += 1
            pq.put(card)
        print(f'pq: {pq.queue}')
        print(f'cnt: {cnt}')
        while not pq.empty():
            while cnt[pq.queue[0]] == 0:
                pq.get()
                print(f'(loop 2) pq: {pq.queue}')
                if pq.empty():
                    return True
            print(f'(loop) pq: {pq.queue}')
            card = pq.queue[0]
            print(f'card: {card}')
            for _ in range(groupSize):
                if cnt[card] == 0:
                    return False
                cnt[card] -= 1
                card += 1
            print(f'end group, cnt: {cnt}')
        return True
            