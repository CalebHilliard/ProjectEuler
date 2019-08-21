target = 600851475143

def next_prime(prime_list):
  number = prime_list[-1]+1
  while(True):
    for prime in prime_list:
      if number % prime == 0:
        break
      elif prime == prime_list[-1]:
        prime_list.append(number)
        return
    number += 1

prime_list = [2]
while target >= prime_list[-1]:
  for prime in prime_list:
    if target % prime == 0:
      target = target/prime
      break
    elif prime == prime_list[-1]:
      next_prime(prime_list)

print(prime_list[-1])
