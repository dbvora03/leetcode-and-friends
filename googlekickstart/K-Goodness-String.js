const kGoodnessString = (s, k) => {
    
  if (s.length <= 1) {
      return 0
  }
  
  let i = 0
  let j = s.length - 1
  
  let score = 0;
  
  while(i < j) {
      if (s[i] != s[j]) {
          score++
      }
  
      i++
      j--
  }
  

  return Math.abs(score - k)
}