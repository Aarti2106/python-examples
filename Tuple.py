t=(1,2,3,"tops","java",[10,20,30],"c","False",1.1,0,1,1,"Ture")

print(t)
print (t.count(1))
print(t.index(1.1))

for i in t:
    print(i)
    
print(1 in t)
print(len(t))
print(t[5])
t[5].append(40)
print(t[5])
t[5].append(50)
print(t[5])
