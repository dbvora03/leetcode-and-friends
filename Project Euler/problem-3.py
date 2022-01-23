def largest_prime():

  number = 600851475143

  i = 2
  while i <= number:
    if number % i == 0:
      while number % i == 0:
        number /= i
        if number == 1:
          return i
    i += 1
  
print(largest_prime())