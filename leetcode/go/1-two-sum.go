package leetcode

func twoSum(nums []int, target int) []int {
    
	cache := make(map[int]int)
	
	for i := 0; i < len(nums); i++ {
			
			value, ok := cache[target - nums[i]]
			
			if ok {
					result := []int{i, value}
					return result
			}
			
			cache[nums[i]] = i
	}
	
	result := []int{-1, -1}
	return result
	
}