
def unique_list(l):
  x = []

  for a in l:
    if a not in x:
      x.append(a)
  return x 
   

res=unique_list([1,1,1,2,2,2,3,3,4,4])   
print res