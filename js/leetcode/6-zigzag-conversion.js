// Yo i deadass did this on my first try
// i am cracked

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
 var convert = function(s, numRows) {
    
  let hash = {}    
  let isDown = true
  let depth = -1
  
  for (let i = 0; i < s.length; i++) {
      
      if (isDown) {
          depth++
      } else {
          depth--
      }
      
      if (!(depth in hash)) {
          hash[depth] = ''
      }
      
      hash[depth] += s[i]
      
      if (isDown && depth == (numRows - 1)) {
          isDown = false
      }
      
      if (!isDown && depth == 0) {
          isDown = true
      }
  }
  
  let answer = ''
  for (const key in hash) {
      answer += hash[key]
  }
  
  return answer
      
};