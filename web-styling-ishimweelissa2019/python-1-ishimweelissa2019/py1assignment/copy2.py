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