'''  take comma(,) seperated list of inttegers as input from the user
print the input list in first line of output
in second line of output remove numbers from the list those are of even status , and the list  
after removing them 
   '''

#ans

l=list(map(int,input().split(",")))
print(l)
s=[]
for i in l:
    if i%2!=0:
        s=s+[i]
print(s)