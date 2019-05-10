def simple_gen():
  for x in range(3):
    yield x

for num in simple_gen():
  print num    

#print the function object simply return memory address
g=simple_gen()
print g

#next function print the one value/num at a time,here it print '0'
print next(g)