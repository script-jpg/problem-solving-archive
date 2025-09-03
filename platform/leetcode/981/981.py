class TimeMap:

    def __init__(self):
        self.key_to_timestamps: Dict[str, List[int]] = defaultdict(list)
        self.key_timestamp_to_value: Dict[Tuple[str, int], str] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timestamps[key].append(timestamp)
        self.key_timestamp_to_value[(key, timestamp)] = value
        
    def get(self, key: str, timestamp: int) -> str:
        # given a list of timestamps associated with keys find the one that is <= timestamp but closest to timestamp
        timestamps = self.key_to_timestamps[key]
        if len(timestamps) == 0:
            return "" # DNE
        if timestamp < timestamps[0]:
            return "" # DNE
        # invariant: timestamps[idx] <= timestamp
        l, r = 0, len(timestamps) - 1
        idx = 0
        while l <= r:
            mid = (l+r)//2
            if timestamps[mid] <= timestamp:
                idx = mid
                l = mid + 1 # try to find largest such solution
            else:
                r = mid - 1
        return self.key_timestamp_to_value[(key, timestamps[idx])]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
