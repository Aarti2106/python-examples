#Ledder if else

sname=(input("Enter student Name :"))
rno=int(input("Enter Roll No :"))
s1=int(input("Enter Marks of subject 1:"))
s2=int(input("Enter Marks of subject 2:"))
s3=int(input("Enter Marks of subject 3:"))

total=s1+s2+s3
per=total/3

print("student name :",sname)
print("Roll No :",rno)
print("Total :",total)
print("percentage :",per)

if per >=70:
    print("Distinction")
elif per >=60:
    print("First class")
elif per >=50:
    print("second class")
elif per >=40:
    print("pass class")
else:
    print("fail")


          
