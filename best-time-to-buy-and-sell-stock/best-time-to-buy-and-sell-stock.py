class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #This clears 198/211 test cases and then throws TLE
        #O(N^2) Time and O(1) Space
        
        """
        
        n=len(prices)
        answer = 0
        for i in range(0 , n):
            for j in range(i + 1 , n):
                if prices[j] > prices[i]:
                    a1 = prices[j] - prices[i] 
                    answer = max(answer, a1)
        return answer             
        
        """
        
        #TAKEN HELP FROM DISCUSSION SECTION
        #O(N) Time and O(1) Space
        
        #We need to find the largest peak following the smallest valley
        
        # Max profit and price to buy
        max_profit = 0 
        high_buy = 0
        
        # Reverse the array of prices
        prices = prices[::-1]
        
        #Check each price to sell as compared to the highest buy price ahead of it
        for price in prices:
            # Update highest buy price in front of price
            if price > high_buy:
                high_buy = price
            # Check if this sale make higher profit than sales later in original array
            if (high_buy - price) > max_profit:
                max_profit = high_buy - price
                
        # Return the highest profit achieved
        return max_profit