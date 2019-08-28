from math import sqrt

def factor_sum(number):
  factors = set()
  for x in range(1, int(sqrt(number))+1):
    if x not in factors:
      if number % x == 0:
        factors.add(x)
        factors.add(int(number/x))
    else:
      break
  total = 0
  for num in factors:
    total += num
  return total-number

abundant_numbers = set()
total = 0

for number in range(1,28124):
  if number < factor_sum(number):
    abundant_numbers.add(number)
  total += number
  for num in abundant_numbers:
    if number - num in abundant_numbers:
      total -= number
      break

print(total)
