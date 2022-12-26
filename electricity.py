unit=int(input("Enter unit:"))
amount=0
if unit<=100:
         amount=0
         print("amount to pay :",amount)
if unit>100 and unit<=200:
         amount=(unit-100)*5
         print("amount to pay :",amount)
if unit>200:
         amount=400+(unit-200)*10
         print("amount to pay :",amount)
