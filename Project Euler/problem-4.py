
def largest_palidrome_product():

  largest = 0

  cache = set()

  for j in range(1000):
    for k in range(1000):
      product = j * k

      if product not in cache:
        cache.add(product)

        string_val = str(product)

        if int(string_val) == int(string_val[::-1]):
          largest = max(largest, product)

  return largest

print(largest_palidrome_product())

