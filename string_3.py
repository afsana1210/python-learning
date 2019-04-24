#Given a string, return a string where for every character in the original there are three characters

def string_3(word):
  
  result=''
  for chars in word:
     result+=chars*3
  return result   



res=string_3('Hello')
print(res)