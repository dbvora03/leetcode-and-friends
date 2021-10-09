/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

 var twoSum = function(nums, target) {

  let hash = {}

  for (let i = 0; i < nums.length; i++) {
    //find a potential number
    let potentialNumber = target - nums[i]

    // if that number exists, then we have our answer
    if (potentialNumber in hash) {
      return [i, hash[i]]
    } else {
      // if not, pop it in here
      hash[nums[i]] = i
    }
  }

}