# OLD MACDONALD- Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def old_macdonald(name):
  if len(name) >3:
   return name[:3].capitalize()+name[3:].capitalize() 
  else:
   return "name is too short" 



res=old_macdonald('macdonald')   
print(res)