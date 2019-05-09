def new_decorator(original_func):
  
  def wrap_func():
    print 'some extra code before the original function'

    original_func()
    print 'some extra code after the original function'

  return wrap_func()

def func_need_decorator():
  print 'i want to be decorated!'

decorator=new_decorator(func_need_decorator)
     
 
   