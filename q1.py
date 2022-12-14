'''
Write a program to enter few strings in a list (Space separated) and then perform the insertion of a separate user
 input string in the list at user specified index.
'''

#ans

list1=[s for s in input().split(' ')]
data=input()
loc=int(input())
list1.insert(loc, data)
print(list1)
