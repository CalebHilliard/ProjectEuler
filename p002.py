target = 4000000

previous_term = 1
current_term = 2
summation = 0

while current_term <= target:
  if current_term % 2 == 0:
    summation += current_term
  current_term += previous_term
  previous_term = current_term - previous_term

print(summation)
