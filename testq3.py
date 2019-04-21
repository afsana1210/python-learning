#go through the string blow and print the word wich is even in len
mystr='print only the word that start with s in this sentence'
newlist=mystr.split()

for word in newlist:
   if len(word)%2==0:
      print(word+"in this sentence")

