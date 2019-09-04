def sieve_of_eratosthenes(target):
  primes = set()
  not_primes = set()

  for x in range(2, target+1):
    if x in not_primes:
      continue
    else:
      primes.add(x)
      for y in range(x*2, target+1, x):
        not_primes.add(y)
  
  return primes

def circular_check(number, primes):
  str_num = str(number)
  for place in range(len(str_num)):
    if int(str_num[place:] + str_num[:place]) not in primes:
      return False
  return True

primes = sieve_of_eratosthenes(1000000)
total = 0

for x in range(2,1000001):
  if circular_check(x, primes):
    total += 1
    
print(total)
