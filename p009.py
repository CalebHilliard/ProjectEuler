def pythagorian_triplet():
  for a in range(2, 1000):
    for b in range(a, 1000):
      c = 1000-a-b
      if a*a + b*b == c*c:
       return(a*b*c)

print(pythagorian_triplet())
