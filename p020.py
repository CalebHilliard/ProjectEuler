def factorial(number):
  if number > 1:
    return factorial(number-1)*number
  else:
    return 1

number = str(factorial(100))
total = 0

for digit in number:
  total += int(digit)

print(total)
