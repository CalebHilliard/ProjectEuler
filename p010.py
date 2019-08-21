def sieve_of_eratosthenes(target):
  primes = []
  not_primes = set()

  for x in range(2, target+1):
    if x in not_primes:
      continue
    else:
      primes.append(x)
      for y in range(x*2, target+1, x):
        not_primes.add(y)
  
  return primes

print(sum(sieve_of_eratosthenes(2000000)))
