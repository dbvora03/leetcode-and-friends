def sum_square_difference():
  first_sum = 0

  for number in range(101):
    first_sum += number*number
  
  second_sum = 0

  for number in range(101):
    second_sum += number
  
  second_sum = second_sum * second_sum

  return second_sum - first_sum

print(sum_square_difference())