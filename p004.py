max_ = 0

for x in range(1000,100,-1):
  for y in range(x+1, 100, -1):
    if str(x*y) == str(x*y)[::-1]:
      if x*y > max_:
        max_ = x*y

print(max_)
