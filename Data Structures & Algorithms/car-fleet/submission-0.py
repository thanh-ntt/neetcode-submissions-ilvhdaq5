import heapq
import bisect

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # fleet's leader <=> higest position
        # a fleet is defined by time <= leader
        n = len(position)
        time = [None] * n
        pos = [None] * n
        processed = [False] * n
        for i in range(n):
            time[i] = ((target - position[i]) / speed[i], i)
            pos[i] = (position[i], i)
        time.sort(key=lambda t: (t[0], position[t[1]]))
        # print(f'time: {time}')
        heapq.heapify_max(pos)
        # print(f'pos: {pos}')
        count = 0
        while pos:
            car_pos, car = heapq.heappop_max(pos)
            # print(f'car_pos {car_pos}, car {car}')
            if processed[car]:
                # print(f'processed: {processed}')
                continue
            count += 1
            time_to_target = (target - car_pos) / speed[car]
            time_idx = bisect.bisect_left(time, (time_to_target, car))
            # print(f'time_to_target {time_to_target}, car {car}, time_idx {time_idx}')
            for i in range(time_idx, -1, -1):
                cur_time, cur_car = time[i]
                if processed[cur_car]:
                    # print(f'break cur_car {cur_car}')
                    break
                # print(f'set processed {cur_car}')
                processed[cur_car] = True
        return count
