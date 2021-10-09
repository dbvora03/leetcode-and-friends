/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */


 var isAnagram = function(s, t) {


  // Check if they are the same length  
  if (s.length != t.length) return false

  let hash = {}
  
  // Count each letter inside the first string
  for (let letter of s)  {
      if(hash[letter]) {
          hash[letter]++
      } else {
          hash[letter] = 1
      }
  }
  

  // Iterate through each letter in other string
  for (let letter of t) {

      if (hash[letter]) { // If letter exists, decrement
          
          hash[letter]--
          
          if (hash[letter] < 0) return false // all hash values should equal to 0 theoretically
      } else {
          return false
      }
  }
  
  return true
  
};