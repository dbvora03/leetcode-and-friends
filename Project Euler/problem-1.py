
def multiples_of_5_or_3():
  answer = 0

  for number in range(3, 1000):
    if number % 5 == 0 or number % 3 == 0:
      answer += number
  
  return answer

print(multiples_of_5_or_3())