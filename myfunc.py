def myfunc(string):
 str1=''

 for i in range(len(string)):
  #if i%2 == 0:
  # str1=str1+string[i].upper() #if string is even make it in upper case.
  if i % 2 == 1:
    str1=str1+string[i].lower() #if sttring is odd make it in lower case.
  return str1   


result=myfunc('AFSA')
print(result)