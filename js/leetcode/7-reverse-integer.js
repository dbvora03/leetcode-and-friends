/**
 * @param {number} x
 * @return {number}
 */

var reverse = function(x) {
    
  let isNegative = x < 0 ? true : false
  
  if(isNegative) x *= -1
  
  let newVar = 0
  
  while(x >= 0) {
      newVar += (x % 10)
      newVar *= 10
      x -= (x % 10)
      x /= 10
  }
  
  newVar /= 10
  
  if(isNegative) newVar *= -1
  
  
  return newVar
};