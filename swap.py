#Wirte python program that swap two number with temp variable and without temp variable.

#with temp swap
a=50
b=20
temp=a
a=b
b=temp
print(a)
print(b)


#without temp swap

a=50
b=20
a,b=b,a
print(a)
print(b)
