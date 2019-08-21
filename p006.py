square_of_sums = 0
sum_of_squares = 0

for x in range(1, 101):
  sum_of_squares += x*x
  square_of_sums += x

square_of_sums *= square_of_sums
answer = square_of_sums - sum_of_squares

print(answer)
