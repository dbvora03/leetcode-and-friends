/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
     
  let stack = []
  let mapping = {
      '(':')',
      '{':'}',
      '[':']'
  }
  
  for (const letter of s) {
      if (letter in mapping) {
          stack.push(letter)
      } else {
          if (mapping[stack.pop()] !== letter) {
              return false
          }
      }
  }

  return stack.length == 0 ? true : false
};