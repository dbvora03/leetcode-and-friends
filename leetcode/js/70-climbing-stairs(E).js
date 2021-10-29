/**
 * @param {number} n
 * @return {number}
 */
 var climbStairs = function(n, cache = {}) {
  if(n == 1) return 1;
  if(n == 2) return 2;
  if(n in cache) return cache[n];
  
  cache[n] = climbStairs(n - 1, cache) + climbStairs(n - 2, cache)
  return cache[n]
};