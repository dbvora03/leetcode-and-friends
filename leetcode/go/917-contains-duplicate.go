package leetcode

func containsDuplicate(nums []int) bool {
  
	cache := map[int]bool{}
	
	for i := 0; i < len(nums); i++ {
			
			_, ok := cache[nums[i]]
			
			if ok {
					return true
			} else {
					cache[nums[i]] = true
			}
	}
	
	return false

}