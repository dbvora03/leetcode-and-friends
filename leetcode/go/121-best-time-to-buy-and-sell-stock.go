package leetcode

func maxProfit(prices []int) int {
        
	lowestCost := 10*10*10*10
	maxProfit := 0;
	
	for i := 0; i < len(prices); i++ {
			
			if prices[i] < lowestCost {
					lowestCost = prices[i]
			} else if prices[i] - lowestCost > maxProfit {
					maxProfit = prices[i] - lowestCost
			}
	}
	
	return maxProfit
}