def hello(name='mady'):
    print 'the hello() function has been executed!' 
    
    def greet():
     return '\t this is the greet() function inside the hello function'

    def welcome():
     return '\t this is the welcome() function inside the hello'

  
    if name == 'mady':
       return greet()
    else:
       return welcome()  
     
my_func=hello('mady') 
print my_func    