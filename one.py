#one.py

def func():
 print 'func() in one.py'

print 'top level in one.py'

#__name__ is a built-in variable which evaluates to the name of the current module.
#  Thus it can be used to check whether the current script is being run on its own or being imported somewhere else by combining it with if statement

if __name__ =='__main__':
  print 'one.py is beign run directly'
else:
  print 'one.py has been imported!'

