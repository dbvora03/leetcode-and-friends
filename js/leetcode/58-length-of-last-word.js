/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLastWord = function(s) {
    
  let count = 0
  let searchingForWord = true
  for(let i = s.length - 1; i >= 0; i--) {
      if (s[i] != ' ' && searchingForWord) {
          searchingForWord = false
          count++
      } else if(s[i] == ' ' && !searchingForWord) {
          return count
      } else if (s[i] != ' ') {
          count++
      }
  }
  
  return count
};