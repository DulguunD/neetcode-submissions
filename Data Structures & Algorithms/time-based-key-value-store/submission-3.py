class TimeMap:

    def __init__(self):
        self.time_map = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        left = 0
        tuple_list = self.time_map[key]
        right = len(tuple_list)-1
      
        while left <= right:
            mid = (left+right)//2
            if tuple_list[mid][1] < timestamp:
                left = mid+1
            elif tuple_list[mid][1] > timestamp:
                right = mid-1
            else:
                return tuple_list[mid][0]

        if timestamp >= tuple_list[right][1]:
            return tuple_list[right][0]

        return ""
        
     