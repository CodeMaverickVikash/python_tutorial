"""
* Variable and Data type
"""
a = 5
strVar = str(a) # type casting
strVar2 = "vikash"
# print(strVar2)
# print(type(a), a)
# print(type(strVar))

"""
* Conditional statements
* if, elif, else
"""
x=10
if x>0:
    print("first string")
elif x>11:
    print("second string")
elif x<0:
    print("third string")
else:
    print("nothing")
    
"""
* Looping
* for, while
"""
x=5
f=1
for i in range(1,x+1):
    f=i*f
print(f)

x=1
while x<=5:
    print("hello")
    x +=1

""" 
* List and it's method
* list are mutable, meaning their elements can be changed.
* list items are changeable, and allow duplicate values.
"""
lis = [12, 23, 56, "hello", "hello"] # Duplicate allow
# lis[0] = 23 # we can change

# add item into list
# lis.append(12)
# lis.insert(1, "Sanu")

# remove item from the list
# lis.remove(23)
# lis.pop(0)
# lis.pop()
# lis.clear()

# iterating over list
# for item in lis:
#     print(item)
# Another way
# for i in range(len(lis)):
#     print(lis[i])

# print(lis)

""" 
* Tuple and it's method
* tuple are immutable, meaning their elements can't be change.
* tuple items are unchangable and allow duplicate values.
"""
tup= ("vikash", "nishant", 12, 23, "vikash") # Duplicate allow
# tup[1] = "Raja" # This will throw error because tuple is unchangable
# print(tup[1])

# iterating over tuple
# for item in tup:
#     print(item)
# another way
# for i in range(len(tup)):
#     print(tup[i])

# print(tup)

""" 
* Sets
* A set is a collection which is unordered, unchangeable, and unindexed.
"""
set_ex = {"sanu", "raja", 12, 23, "sanu"} # does not allow duplicates

# iterating over sets
# for item in set_ex:
#     print(item)

# print(set_ex)

""" 
* Dictionary
* dictionary doesn't allow duplicate values.
"""
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

"""
* Exception Handling
* try, except, else, finally blocks
"""
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

'''
* Functions 
'''
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
