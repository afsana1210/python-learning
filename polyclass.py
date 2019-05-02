def Dog():
  
  def __init__(self,name):
    self.name=name

  def speak(self):
     return self.name+"say woof!" 

def Cat():
  
  def __init__(self,name):
    self.name=name

  def speak(self):
     return self.name+"say meow!"


niko=Dog()
#print niko.speak()

felix=Cat()
#print felix

for pet in [niko,felix]:
 print type(pet)
 print type(pet.speak())

def pet_speak(pet):
 print pet.speak()

print pet.speak(niko)
print pet_speak(felix)