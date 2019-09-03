upper_bound = 1

#The upper bound of the solution is constrained by
#the point where 9^5 * x has x or more digits
while(True):
  if upper_bound >= len(str(upper_bound * 9**5)):
    break
  upper_bound += 1

sum_ = 0

for number in range(10,upper_bound * 9**5):
  total = 0
  for digit in str(number):
    total += int(digit)**5
  if total == number:
    sum_ += number

print(sum_)
