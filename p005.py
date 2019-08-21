def factorize(number, prime_list):
  factors = []
  while number > 1:
    for prime in prime_list:
      if number % prime == 0:
        factors.append(prime)
        number = number/prime
        break
  return factors

factorization_list = []
total = 1
prime_list = [2,3,5,7,11,13,17,19]
max_number = {}

for x in range(2, 21):
  factorization_list.append(factorize(x, prime_list))
for prime in prime_list:
  max_number[prime] = 0

for list_ in factorization_list:
  for prime in prime_list:
    x = sum(y == prime for y in list_)
    if x > max_number[prime]:
      max_number[prime] = x

for amount in max_number:
  total *= amount**max_number[amount]

print(total)

#A number is divisibal by another number without
#remainder if the smaller number shares all prime
#factors with the larger number. By finding the largest
#number of each prime within the prime factors of 1-20
#we can create the prime factorization of our answer
