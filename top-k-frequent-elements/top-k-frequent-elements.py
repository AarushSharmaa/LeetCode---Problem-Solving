class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        # 1 <= k <= len(set(nums))
        if n == 1 and k == 1:
            return nums
        
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
                
        #dictionary stores elements and their frequency in the form of key value pair  : {1 : 3, 2 : 2, 3 : 1}
            
        arr = []
        for i in dictionary:
            arr.append(dictionary[i]) #[3, 2, 1]
        #arr contains the frequency of each element
        #sorting them in reverse order will contain frequencies of element in decreasing order
        
        
        arr.sort(reverse = True)#[3, 2, 1]
        
        #now, we have to retrieve values corresponding to first k elements of arr
        output = []
        index = 0
        count = 0 
        for i in range(0, k):
            for key, value in dictionary.items():
                if arr[i] == value:
                    if key not in output:
                        output.append(key)
                        break

        return output
        
        
                
        