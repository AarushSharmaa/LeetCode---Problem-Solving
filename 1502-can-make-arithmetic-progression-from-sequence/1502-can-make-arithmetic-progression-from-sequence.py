class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        temp = arr[0] - arr[1]
        n = len(arr)
        for i in range(1, n - 1):
            distance = arr[i] - arr[i + 1]
            if distance != temp:
                return False
        return True