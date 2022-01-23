def special_pythagorean_triplet():

  for c in range(1000):
    for b in range(c):
      for a in range(b):

        if a*a + b*b == c*c and a + b + c == 1000:
          return a*b*c
  
  return "not found"


print(special_pythagorean_triplet())