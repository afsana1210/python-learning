#inheritance

def Animal():

   def __init__(self):
    print('animal created')

   def who_am_i(self):
    print('i am a animal')

   def eat(self):
     print('i am eating')
#inherit the properties and behaviour of class animal by writing the animal class inside the dog class parenthesis.
def Dog(Animal):

  def __init__(self): 
   Animal.__init__(self)
   print('dog created')
  
  #method overriding
  def who_am_i(self):
    print('i am a dog')

  def eat(self):
     print('i am dog and eating')  


mydog=Animal()
print mydog.eat()  

#mydog.eat()
