class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        if n < 3:
            return []
        
        #A very important statement : Notice that the solution set must not contain duplicate triplets.
        mat = []
        nums.sort() #sorting this will allow us to use 2 - pointers approach
        #if it only contained positive elements, maybe we did not need to sort
        
        #we will use the equation nums[j] + nums[k] = -nums[i]
        #we will fix -1 * nums[i] and use 2 pointer approach to find nums[j] and nums[k]
        #basically, once we fixed -nums[i], we have to find if (nums[j] + nums[k]) exists in array or not
        for i in range(0, n):  
            
            if i > 0 and nums[i] == nums[i-1]: #taking care of duplicates at the level of nums[i]
                continue
            
            else:
                remaining_sum = -1 * nums[i] #fixing one element
                p1 = i + 1 #1st pointer for nums[j]
                p2 = n - 1 #2nd pointer for nums[k]
                 
                while (p1 < p2): #termination coniditon - equality sign not added as it can be a possible scenario
                    arr = []
                    current_sum = nums[p1] + nums[p2]
                    
                    #Case 1
                    if current_sum < remaining_sum :
                        p1 += 1
                        
                    #Case 2
                    elif current_sum > remaining_sum :
                        p2 -= 1
                    
                    #Case 3 
                    #add the values
                    #move across duplicates
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
                    
        
        
 