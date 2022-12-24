''' Nested if else '''
a=int(input ("Enter A:"))
b=int(input ("Enter B:"))
c=int(input ("Enter C:"))

if a>b:
    if a>c:
          print(a,"Is greater number")

    else:
       print(c,"Is greater number")
elif b>c:
        print(b,"Is greater number")
else:
       print(c,"Is greater number")
   
