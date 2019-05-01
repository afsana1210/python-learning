class Dog:
    def __init__(self,Dbreed,name,spots):

        
        #ATTRIBUTES
        #WE TAKE IN THE ARGUMENTS
        #AND ASSIGN IT WITH SELF.ATTRIBUTES_NAME
        self.Dbreed=Dbreed
        self.name=name
        #EXPECT BOOLEAN TRUE/FALSE
        self.spots=spots

        #operation/action -->method
    def bark(self,number):
     print('woof!my name is {} and number is{} '.format(self.name,number))    
my_dog=Dog(Dbreed='lab',name='tom',spots='False')
print(my_dog.Dbreed)
my_dog.bark(10)
