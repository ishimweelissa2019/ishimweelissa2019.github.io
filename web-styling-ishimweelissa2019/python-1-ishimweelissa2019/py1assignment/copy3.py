numbers=[]
i = 2000
while i <= 3200:
  if i % 7 ==0 and i%5 !=0:
    numbers.append(str(i))
    
  i += 1  
print (','.join(numbers)) 