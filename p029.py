found_values = set()

for a in range(2, 101):
  for b in range(2,101):
    number = a**b
    if number not in found_values:
      found_values.add(number)

print(len(found_values))
