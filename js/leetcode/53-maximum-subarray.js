/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {

  let totalMax = nums[0]
  let currentMax = 0;
  
  
  for (const number of nums) {
      currentMax += number
      
      if (currentMax < number) {
          currentMax = number
      }
      
      totalMax = Math.max(totalMax, currentMax)
      
  }
  
  return totalMax
  
};