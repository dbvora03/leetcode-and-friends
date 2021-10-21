const increasingSubstring = (num, str) => {
    
  let answer = [1]
  
  for(let i = 1; i < num; i++) {
      
      if (str[i] < str[i - 1]) {
          answer.push(1)
      } else {
          answer.push(answer[i - 1] + 1)
      }
  }
  return answer
}