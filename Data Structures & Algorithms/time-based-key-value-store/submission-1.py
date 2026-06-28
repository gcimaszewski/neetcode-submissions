class TimeMap:

    def __init__(self):
        self._map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # all timestamps of set are strictly increasing, 
        # so simply appending to a list will keep their order
        if key not in self._map:
            self._map[key] = []
        self._map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # n = num. values associated with key
        # m: total num. keys
        # want O(log n) complexity
        # binary search for closest ts_prev such that ts_prev <= timestamp?
        if key not in self._map:
            return ""
        vals_for_key = self._map[key]
        left = -1
        right = len(vals_for_key)
        # invariant:
        # for i <= left, vals[i].ts <= timestamp
        # for j >= right: vals[j].ts > timestamp
        while left + 1 < right:
            mid = left + (right - left)//2
            ts, val = vals_for_key[mid]
            if ts > timestamp:
                right = mid
            else:
                left = mid
        if left > -1:
        # value to return sits at index `left`
            return vals_for_key[left][1]
        else:
            return ""
