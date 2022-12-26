s=(input("Enter string:"))

ch=0
w=1
sp=0
n=0
sc=0


for i in s:
    if i.isalpha():
        ch=ch+1
    elif i.isspace():
        w=w+1
        sp=sp+1
    elif i.isnumeric():
        n=n+1
    else:
        sc=sc+1
print("total character :",ch)
print("total word:",w)
print("total space:",sp)
print("total number:",n)
print("total special character:",sc)
