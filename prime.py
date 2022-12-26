n=int(input("Enter numbr :"))
primeFlag = True;

if n < 2:
  primeFlag = False

else:
  for i in range(2, n):
    if n%i == 0 and n != i:
         primeFlag = False;

print("Is Prime:",primeFlag)
