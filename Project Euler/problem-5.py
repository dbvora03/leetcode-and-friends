
def smallest_multiple():

  number = 60000000
  while True:

    div_by_all = True
    for i in range(1, 21):
      if number % i != 0:
        div_by_all = False
        break
    
    if div_by_all:
      return number
    else:
      number += 1

print(smallest_multiple())
