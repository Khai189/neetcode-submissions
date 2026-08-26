class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        
        else:
            self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
        
        else:
            arr = self.store[key]
            left, right = 0, len(arr) - 1
            ans = ""
            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid][0] == timestamp:
                    return arr[mid][1]
                
                elif arr[mid][0] > timestamp:
                    right = mid - 1
                
                else:
                    ans = arr[mid][1]
                    left = mid + 1
            

            return ans


        
