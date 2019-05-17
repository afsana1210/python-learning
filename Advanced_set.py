#Advanced set
s=set()
s.add(1)
s.add(2)
print s
s.add(2) #dublicate value is not allowed in set
print s
sc=s.copy()
print sc
s.add(3)
print s
d=s.difference(sc)
print d
