# Working with file
'''
"r" - open file for reading - default("rt")
"w" - open file for writing
"x" - create file if not exist
"a" - add more content to a file
"t" - text mode
"b" - binary mode
"+" - read and write
'''

# Reading File
# f = open("vikash.txt", "rt")
# f = open("oops.py", "rt")

# content = f.read()
# print(content)

# for line in f:
#     print(line, end="")

# f.close()

# Writing and Appending to file
# f = open("vikash.txt", "w")
# f = open("vikash.txt", "a")

# # f.write("Vikash is do not need to fear.")
# f.write("Sanu is good boy.")

# f.close()

# Shortcut 
# with open("vikash.txt", "a") as f:
#     f.write("Hello World!!!")

# Handle read and write both
# f = open("vikash.txt", "r+")
# print(f.read())
# f.write("this is me\n")
# f.close()
