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

target = 10001
prime_list = [2]
for x in range(1,target):
  next_prime(prime_list)
print(prime_list[-1])
