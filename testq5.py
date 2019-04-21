#use list comprehension to create a list of first letter in the string 
mystr='print only the word that start with s in this sentence'

l=[word[0] for word in mystr.split()]
print(l)