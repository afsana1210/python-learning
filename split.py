mystr='print only the word, that start with s in this sentence'
#newlist=mystr.split('s')

for letter in mystr.split(','):
 """ if letter[0]=='s':"""   
 print(letter)
"""start
s
sentence
"""
#if letter s is capital
mystr='S print only the word that start with s in this sentence'
#newlist=mystr.split('s')

for letter in mystr.split():
  if letter[0].lower()=='s':   
    print(letter)










#list comprehension to create list of the number which is divisible by 3.
mylist=[x for x in range(1,51) if x%3==0 ]
print(mylist)










for num in range(0,100):
  if num%3==0 and num%5==0: 
    print('fizzbuff',num)
  elif num%3==0:
    print("fizz",num)
  elif num%5==0:
    print("buzz",num)
  
  #else:("not");  
  """fizz
fizz
buzz
fizz
fizz
buzz
fizz
fizz
fizz
buzz
fizz
fizz
buzz
fizz
fizz
fizz
buzz
fizz
fizz
buzz
fizz
fizz
fizz
buzz
fizz
fizz
buzz
fizz
fizz
fizz
buzz
fizz
fizz
buzz
fizz
fizz
fizz
buzz
fizz
fizz
buzz
fizz
fizz
fizz
buzz
fizz
fizz"""


