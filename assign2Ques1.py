'''Ques.1.For a given input string “Python is a case sensitive language”. Write python 
code for the following:
a. Find the length of the input string.
b. Reverse the order of the string in one line code.
c. Using Slice function store “a case sensitive” in new string.
d. Replace “a case sensitive” with “object oriented”.
e. Find index of substring “a” in the given input string.
f. Remove the white spaces from the given input string.'''
#the input Python is a case sensitive language as string
x="Python is a case sensitive language"
#a
y=len(x)
print("length of string =",y)
#b
z=x[::-1]
print(z)
#c
replaced=x.replace("a case sensitive","object oriented")

print(replaced)
#d
print(x.index("a"))
#e
print(x.replace(" ",""))
#ece22105015

