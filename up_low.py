#write a function  that accept a string and calculate the upper case letter and lower case letter.

s="Hello Mr.X. "

def up_low(s):
  d={'upper':0,'lower':0}
  for c in s:
   if c.isupper():
    d['upper']+=1
   elif c.islower():
    d['lower']+=1
   else:
    pass
  print 'orignal string ',s
  print 'no of upper case characters:' ,d['upper']
  print 'no of lower case characters:' ,d['lower']


up_low(s)  