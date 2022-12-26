d={1:"rajveer",2:"bhavesh",3:"jay",4:"vipul",5:"bhavdeep",6:"manav"}

print(d[3])
d1=d.copy()
print(d1)
d1[7]="rignesh"
print(d1)
print(d)
d2=d
d2[8]="arti"
print(d2)
print(d)
print(d.get(4))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(3))
print(d)
print(d.popitem())
d3={10:"arti",11:"jay",12:"rashik"}
d.update(d3)
print (d)

for i in d:
    print(i," : ",d[i])
