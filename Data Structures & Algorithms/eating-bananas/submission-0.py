class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k):
            s = 0
            for pile in piles:
                if pile % k == 0:
                    s += pile / k
                else:
                    s += pile // k + 1
            # print(f'can_eat {k} - {s <= h}')
            return s <= h
        def binary_search(l, r):
            if l > r:
                return -1
            elif l == r:
                return r
            m = (l + r) // 2
            if can_eat(m):
                return binary_search(l, m)
            else:
                return binary_search(m + 1, r)
        return binary_search(1, max(piles))
