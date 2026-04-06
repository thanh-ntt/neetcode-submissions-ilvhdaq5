from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = defaultdict(list)
        for t in tickets:
            flights[t[0]].append([t[1], True])
        itinerary = []
        def dfs(src) -> bool:
            itinerary.append(src)
            for dest in sorted(flights[src]):
                if not dest[1]:
                    continue
                dest[1] = False
                valid = dfs(dest[0])
                if valid:
                    return True
                dest[1] = True
            if len(itinerary) == len(tickets) + 1:
                return True
            else:
                itinerary.pop()
                return False

        dfs('JFK')
        return itinerary