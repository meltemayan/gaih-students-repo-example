num1 = 1
num2 = 100
primes = []

for num in range(num1,num2 + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           primes.append(num)

import random

row = range(3)
mat = []
for i in range(3):
  row = []
  for j in range(3):
    row.append(random.choice(primes))
  mat.append(row)
  print(mat[i])
