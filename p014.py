def chain_len(number):
  count = 0
  while number>1:
    if number % 2 == 0:
      number /= 2
      count += 1
    else:
      number = 3*number + 1
      count += 1
  return count

max_chain = 0
max_n = 0

for n in range(1, 1000000):
  length = chain_len(n)
  if length > max_chain:
    max_chain = length
    max_n = n

print(max_n)
