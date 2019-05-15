#python debugger(pdb)
import pdb
x=[1,2,3]
y=2
z=5

result=y+z
print result
pdb.set_trace()
result1=x+y
print result1