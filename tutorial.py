# Variables in python

# a = 5
# castingIntoStr = str(a)
# str = "vikash"
# print(str)
# print(type(a), a)
# print(type(castingIntoStr))

# Data type

# List items are ordered, changeable, and allow duplicate values.
lis = [12, 23, 56, "hello", "hello"] # Duplicate allow
# lis[0] = 23 # we can change

# add
# lis.append(12)
# lis.insert(1, "Sanu")

# remove
# lis.remove(23)
# lis.pop(0)
# lis.pop()
# lis.clear()

# iterating item
# for item in lis:
#     print(item)
# another way
# for i in range(len(lis)):
#     print(lis[i])

# print(lis)

tup= ("vikash", "nishant", 12, 23, "vikash") # Duplicate allow
# tup[1] = "Raja" # This will throw error because tuple is unchangable
# print(tup[1])

# iterating item
# for item in tup:
#     print(item)

# another way
# for i in range(len(tup)):
#     print(tup[i])

# print(tup)

# A set is a collection which is unordered, unchangeable, and unindexed.
set_ex = {"sanu", "raja", 12, 23, "sanu"} # does not allow duplicates

# iterating item
# for item in set_ex:
#     print(item)

# print(set_ex)

dic = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 1964,
} # does not allow duplicates

# x = dic["model"]
# x = dic.get("model") # same result
# x = dic.keys()
x = dic.values()
print(x)

# print(dic)

# Python Operators

# import array as arr
# a = arr.array('i', [1,2,3]) 
# for i in range(0,3): 
#     print (a[i], end =" ") 
# def home():
#     print("this is function")
# home()



# if and else(decision making)
x=10
if x>0:
    print("first string")
elif x>11:
    print("second string")
elif x<0:
    print("third string")
else:
    print("nothing")

# try and except keyword
num = input("Enter any number: ")
try:
    number = float(num)
except:
    print(number)
else:
    check = number%2
    if check == 0:
        print(int(number), "is an even number.")
    elif check == 1:
        print(int(number), "is an odd number.")
    else:
        print(number, "is strange.")

# for loop
x=5
f=1
for i in range(1,x+1):
    f=i*f
print(f)

# while Loop
x=1
while x<=5:
    print("hello")
    x +=1

x=int(input("enter no. you want to fact"))
i=1
f=1
while i<=x:
    f=i*f
    i+=1
print(f)

x=1
while x<=101:
    if x%3==0:
        print(x)
    x +=1

x=int(input("enter first number"))
while True:
    y=int(input("enter second number"))

    if x==y:
        print("number is match")
        break
# function
def f1():
    print("hello")
f1() # take nothing, return nothing

def f2(name):
    print("hello",name)
f2("vikash") # take something, return nothing

def f3(x,y):
    z=x+y
    return z
a=f3(2,4) # take something, return something
print(a)

def f4():
    return("hello python")
a=f4()# take nothing, return something
print(a)
