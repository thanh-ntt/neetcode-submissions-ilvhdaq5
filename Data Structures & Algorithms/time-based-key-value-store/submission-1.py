import bisect
class TimeMap:
    kv = {}

    def __init__(self):
        kv = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = [(timestamp, value)]
        else:
            self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""
        else:
            v = bisect.bisect_right(self.kv[key], timestamp, key=lambda x: x[0]) - 1
            if v < 0:
                return ""
            # print(f'key: {key}, ts: {timestamp} -> v: {v}, kv[key]: {self.kv[key]}')
            return self.kv[key][v][1]
        
