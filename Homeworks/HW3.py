def primefirst(x):
  for num in range(x,x + 1):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
        print(num) 
          
def primesecond(x):  
  for num in range(x,x + 1):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
              break
       else:
         print(num)
           
for i in range(1000):
  if i < 500:
    primefirst(i)
  else:
    primesecond(i)
