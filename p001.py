target = 1000
summation = 0

for x in range(0, target):
  if x % 3 == 0:
    summation += x
  elif x % 5 == 0:
    summation += x

print(summation)
