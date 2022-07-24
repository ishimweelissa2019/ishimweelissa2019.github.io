[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8144652&assignment_repo_type=AssignmentRepo)
# C# Coding Challenge.

- **Name**:  ISHIMWE ELISSA
- **Registration Number**:220012479

## Problem Challenges

Problem 1: Given a list of integers, use a for-loop to find its maxi-
mum element; then do the same to find its minimum element.
solution
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

Problem 2. Write a program which checks if a string is palindromic
solution
list1=[]
for i in range(1):
    x = (input("Enter word: "))
w = ""
for i in x:
    w = i + w

if (x == w):
    print("This is Parindrome")
else:
   print("This is not Parindrome")


Problem 3: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
solution
numbers=[]
i = 2000
while i <= 3200:
  if i % 7 ==0 and i%5 !=0:
    numbers.append(str(i))
    
  i += 1  
print (','.join(numbers)) 

Problem 4. Given a list of integers, how many of its elements are
multiples of 3? For example, given the list [5, 6, 9, 10, 15, 17, 18, 21],
five of its elements are multiples of 3.
solution
mult=[3,7,9,12,5,23,21]
a=0
for x in mult:
    if x%3==0:
       a+=1
print(a,"Elements are multiple of three.")

Problem 5. Given a list of integers, can you find the runner-up? For
example, given [2, 3, 3, 6, 4, 5], the maximum is 6 and the runner-up
is 5.
solution
runn=[2,3,3,4,5,6]
runn.sort()
print("The runn-up is:",runn[len(runn)-2])

Problem 6. You are given an un-ordered array consisting of integers
without any duplicates. You are allowed to swap any two elements.
You need to find the minimum number of swaps required to sort the
array in ascending order
solution

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

Problem 7:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
solution
 print("Enter a sequence separated by , here: ")
 value = []
 items=[x for x in input().split(',')]
 for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

 print(','.join(value))


Problem 8. Count the word frequencies in this sentence then create another list without duplicates and sorted by words with more frequencies first.
sonnet1 = [’from’, ’fairest’, ’creatures’, ’we’, ’desire’, ’
increase’,’that’, ’thereby’, ’beauty’,’rose’, ’might’,’
never’, ’die’,’but’,’as’, ’the’, ’riper’, ’should’, ’by’,
’time’, ’decease’,’his’, ’tender’, ’heir’, ’might’, ’
bear’, ’his’, ’memory’,’but’,’thou’, ’contracted’, ’to’,
’thine’, ’own’, ’bright’,’eyes’,’feed’,’thy’,’light’, ’
flame’, ’with’,’self-substantial’,’fuel’,’making’,’a’,’
famine’,’where’, ’abundance’,’lies’,’thyself’,’thy’,’foe’, 'we',
, ’to’, ’thy’, ’sweet’, ’self’, ’too’, ’cruel’]
solution
from collections import Counter
list1 = ['from', 'fairest', 'creatures', 'we', 'desire', 'increase','that', 'thereby', 'beauty','rose', 'might',
       'never', 'die','but','as', 'the', 'riper', 'should', 'by', 'time', 'decease','his', 'tender', 'heir', 'might','bear', 'his', 'memory','but','thou', 'contracted', 'to',
'thine', 'own', 'bright','eyes','feed','thy','light','flame', 'with','self-substantial','fuel','making','a',
'famine','where', 'abundance','lies','thyself','thy','foe', 'we', 'to', 'thy', 'sweet', 'self', 'too', 'cruel']
counts = Counter(list1)
print(counts)


## Additional Info
- For more info & support you can always reach me via MS Teams.



