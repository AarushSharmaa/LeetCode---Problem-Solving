#User function Template for python3

class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        import heapq 
        heap = []
        for i in range(0, len(arr)):
            heapq.heappush(heap, (arr[i][0], i, 0))
        
        count = 0
        final = []
        while count < K * K:
            magnitude, i, j = heapq.heappop(heap)
            final.append(magnitude)
            if (j + 1) < len(arr):
                heapq.heappush(heap, (arr[i][j+1], i, j + 1))
            count += 1 
        return final
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
# } Driver Code Ends