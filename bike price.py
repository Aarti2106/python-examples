'''write a program to accept the cost price of a bike and display the road tax bepaid according to the
following criteria :'''


tax=0
pr=int(input("Enter the price of bike "))

if pr>100000:
    tax=15/100*pr
    print("Tax to be paid",tax)
elif pr>50000 and pr <=100000:
    tax=10/100*pr
    print("Tax to be paid",tax)
else:
    tax=5/100*pr
    print("Tax to be paid",tax)
    

