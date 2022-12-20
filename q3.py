''' 
Write a Python program that asks the user to enter
 a text and return user a dictionary whose keys are the words of the text entered and the values are
 the thrice of the reverse of the words that make up the text.
 '''

w=input().split()
d={}
for i in w:
    d[i]=(i*3)[::-1]
print(d)