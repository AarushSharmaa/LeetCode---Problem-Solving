class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        #first, get all the valid points in an array 
        #if no valid points, return -1
        #else, return the smallest valid point's distance from my current location 
        
        d = {}
        index = 0
        for subarray in points:
            if subarray[0] == x or subarray[1] == y:
                distance = abs(subarray[0] - x) + abs(subarray[1] - y)
                d[index] = distance
            index += 1
            
        if len(d) == 0:
            return -1
        
        minm = min(d.values())
        for index in d:
            if d[index] == minm:
                return index