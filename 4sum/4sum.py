class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        mat = []
        nums.sort()
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n):
                
                if j > (i + 1) and nums[j] == nums[j-1]:
                    continue
                
                #nums[a] + nums[b] + nums[c] + nums[d] = target
                #making it similar to Two Sum Problem, where nums[a] + nums[b] = target
                #we fixed nums[a] and started looking for nums[b] = target - nums[a] 
                #using a dictionary as the given array was unsorted 
                
                #In this question : nums[a] + nums[b] + nums[c] + nums[d] = target
                #fixing nums[a] and nums[b], we will have nums[c] + nums[d] = target - (nums[a] + nums[b])
                remaining_sum = (target - (nums[i] + nums[j]))
                p1 = j + 1
                p2 = n - 1
                while p1 < p2:
                    arr = []
                    current_sum = nums[p1] + nums[p2]
                    
                    if current_sum < remaining_sum : 
                        p1 += 1
                    elif current_sum > remaining_sum:
                        p2 -= 1
                    else:
                        arr.append(nums[p1])
                        arr.append(nums[p2])
                        arr.append(nums[i])
                        arr.append(nums[j])
                        mat.append(arr)
                        
                        if nums[p1] == nums[p2]:
                            break
                        else:
                            x = nums[p1]
                            y = nums[p2]
                            while nums[p1] == x:
                                p1 += 1
                            while nums[p2] == y:
                                p2 -= 1
        return mat
                        