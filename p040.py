string = ""
count = 1

while len(string) < 1000000:
  string += str(count)
  count += 1

#This is a little more readable than one line
d1 = int(string[1-1])
d10 = int(string[10-1])
d100 = int(string[100-1])
d1000 = int(string[1000-1])
d10000 = int(string[10000-1])
d100000 = int(string[100000-1])
d1000000 = int(string[1000000-1])

print(d1*d10*d100*d1000*d10000*d100000*d1000000)
