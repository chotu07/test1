a=1
even=[]
odd=[]
while a<=10:
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
    a=a+1
print(even)
print(odd)
