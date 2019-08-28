num1 = 1
num2 = 1
count = 2

while len(str(num2)) < 1000:
  num2 += num1
  num1 = num2-num1
  count += 1

print(count)
