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
Python program to checkif a string is palindrome or not

2 list1=[]
for i in range(1):
    x = (input("Enter word: "))
w = ""
for i in x:
    w = i + w

if (x == w):
    print("This is Parindrome")
else:
   print("This is not Parindrome")
#3check list

#4
mult=[3,7,9,12,5,23,21]
a=0
for x in mult:
    if x%3==0:
       a+=1
print(a,"Elements are multiple of three.")
#5
runn=[2,3,3,4,5,6]
runn.sort()
print("The runn-up is:",runn[len(runn)-2])
3# nl=[]
# for x in range(2000, 3200):
#     if (x%7==0) and (x%5!=0):
#         nl.append(str(x))
# print (','.join(nl))
 print("Enter a sequence separated by , here: ")
 value = []
 items=[x for x in input().split(',')]
 for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

 print(','.join(value))
8 from collections import Counter
list1 = ['from', 'fairest', 'creatures', 'we', 'desire', 'increase','that', 'thereby', 'beauty','rose', 'might',
       'never', 'die','but','as', 'the', 'riper', 'should', 'by', 'time', 'decease','his', 'tender', 'heir', 'might','bear', 'his', 'memory','but','thou', 'contracted', 'to',
'thine', 'own', 'bright','eyes','feed','thy','light','flame', 'with','self-substantial','fuel','making','a',
'famine','where', 'abundance','lies','thyself','thy','foe', 'we', 'to', 'thy', 'sweet', 'self', 'too', 'cruel']
counts = Counter(list1)
print(counts)
3 numbers=[]
i = 2000
while i <= 3200:
  if i % 7 ==0 and i%5 !=0:
    numbers.append(str(i))
    
  i += 1  
print (','.join(numbers)) 

def minSwaps(array):
    n = len(array)
    arrpos = [*enumerate(array)]
    arrpos.sort(key = lambda it : it[1])
    vis = {k : False for k in range(n)}
    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans
array = [149, 60, 44, 83, 92]
print(minSwaps(array))
def minSwaps(array):
    n = len(array)
    arrpos = [*enumerate(array)]
    arrpos.sort(key = lambda it : it[1])
    vis = {k : False for k in range(n)}
    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans
array = [149, 60, 44, 83, 92]
print(minSwaps(array))

