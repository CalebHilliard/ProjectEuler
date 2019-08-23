def get_factors(number):
  factors = set()
  for x in range(1, number):
    if x not in factors:
      if number % x == 0:
        factors.add(x)
        factors.add(int(number/x))
    else:
      break
  return factors

triangle_number = 0
count = 1

while True:
  triangle_number += count
  count += 1
  if len(get_factors(triangle_number)) > 500:
    print(triangle_number)
    break
