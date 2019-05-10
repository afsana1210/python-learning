#simple program
def create_cube(n):
  result=[]
  for i in range(n):
    result.append(i**3)
  return result

num=create_cube(10) 
print num

#using generator the below program 

def create_cube(n):

  for i in range(n):
    yield i**3


n=list(create_cube(10)) 
print n


