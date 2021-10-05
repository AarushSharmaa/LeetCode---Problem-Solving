class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        if n < 3:
            return []
        
        #A very important statement : Notice that the solution set must not contain duplicate triplets.
        mat = []
        nums.sort()
        for i in range(0, n):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            else:
                remaining_sum = -1 * nums[i]
                p1 = i + 1
                p2 = n - 1
                while (p1 < p2):
                    arr = []
                    current_sum = nums[p1] + nums[p2]
                    if current_sum < remaining_sum :
                        p1 += 1
                        
                    elif current_sum > remaining_sum :
                        p2 -= 1
                    
                    else:
                        arr.append(nums[i])
                        arr.append(nums[p1])
                        arr.append(nums[p2])
                        mat.append(arr)
                        
                        if nums[p1] == nums[p2]:
                            break
                            
                        x = nums[p1]
                        y = nums[p2]
                        while nums[p1] == x:
                            p1 += 1
                        while nums[p2] == y:
                            p2 -= 1
        return mat
                    
        
        
 