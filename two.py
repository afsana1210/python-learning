#two.py

import one

print 'top level in two.py'

one.func()

if __name__ == '__main__':
 print 'two.py is beign run directly'
else:
  print 'two.py has been imported!'
