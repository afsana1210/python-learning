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
s.discard(2)
print s
d=s.difference(sc)
print d
s1={1,2,3}
s2={1,4,5}
s1.difference_update(s2)
print s1
print s1.intersection(s2)
print s1.intersection_update(s2)
print s1.isdisjoint(s2)



