def hello():
  return 'Hi Jose'

def other(some_other_func):
   print 'other code run here'
   print(some_other_func())

other(hello)     
 