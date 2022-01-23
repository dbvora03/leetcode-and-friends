def even_fib():

  a, b = 1, 1
  answer = 0

  while a < 4000000:
    if (a + b) % 2 == 0:
      answer += (a + b)
    
    a, b = b, a + b

  return answer

print(even_fib())

