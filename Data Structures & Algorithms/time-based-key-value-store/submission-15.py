class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value_list = self.hashmap[key]
        
        l, r = 0, len(value_list) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            
            if value_list[mid][1] <= timestamp:
                res = value_list[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
