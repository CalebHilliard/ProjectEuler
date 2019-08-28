from math import sqrt

def get_factors(number):
  factors = set()
  for x in range(1, int(sqrt(number))):
    if x not in factors:
      if number % x == 0:
        factors.add(x)
        factors.add(int(number/x))
    else:
      break
  return factors

def d(number):
  total = 0
  factors = get_factors(number)
  for thing in factors:
    total += thing
  return total-number

amiable_numbers = []
found_d_values = {}
total = 0

for number in range(1,10000):
  d_value = d(number)
  if d_value in found_d_values:
    if found_d_values[d_value] == number:
      amiable_numbers.append(d_value)
      amiable_numbers.append(number)
  found_d_values[number] = d_value

for number in amiable_numbers:
  total += number

print(total)
