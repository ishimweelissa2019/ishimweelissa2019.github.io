integers=[450,8,2,3,900,400,1,7]
maxi =integers[0]
mini=integers[0]
for n in integers:
    if n>maxi:
        maxi=n
    if n<mini:
        mini=n
print("The maximum number is:",maxi) 
print("The minumum number is:",mini) 