"""Ques6:-For any three lengths, there is a simple test to see if it is possible to form a 
triangle. If any of the three lengths is greater than the sum of the other two, 
then you cannot form a triangle. Otherwise, Enter three sides of a triangle, 
converts them to integers, and to check whether the given input lengths can 
form a triangle or not (Print : “Yes” or “No”)"""
#taking input 
a = input("Type length of side a: ")
b = input("Type length of side b: ")
c = input("Type length of side c: ")
#converting into intgers
z=int(a)
x=int(b)
y=int(c)
#checking the condition
if z > x + y         :
        print("No")
elif x > z+ y   :  
        print("No")
elif y> z + x   :
        print("No")
else:
        print("Yes")
 
  #ece 22105015 
  
