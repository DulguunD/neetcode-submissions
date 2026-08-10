class TimeMap:

    def __init__(self):
        self.time_map = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]
        # print(f"Updated Map: {self.time_map}")
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        left = 0
        tuple_list = self.time_map[key]
        right = len(tuple_list)-1
        # print("\n")
        # print(f"List: {self.time_map}")
        # print(f"\tSearching in the list: {tuple_list}, target: {timestamp}")
        while left <= right:
            mid = (left+right)//2
            # print(f"left: {tuple_list[left]}, right: {tuple_list[right]}, mid: {tuple_list[mid]}")

            if tuple_list[mid][1] < timestamp:
                left = mid+1
            elif tuple_list[mid][1] > timestamp:
                right = mid-1
            else:
                return tuple_list[mid][0]

        # print(f"right timestamp: {tuple_list[right][1]}")
        # print(f"left: {left}, right: {right}")
        if timestamp >= tuple_list[right][1]:
            return tuple_list[right][0]
        
        if timestamp >= tuple_list[left][1]:
            return tuple_list[left][0]

   
        return ""
        
     