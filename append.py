mystring='hello'
#append the string .that mean create empty list and add the string into that list. 
mylist=[]

for letter in mystring:
   mylist.append(letter)

print(mylist)



#list comprehension
#same as above code but simple one line cod .
#here letter is an element after for same element is use and then some object or string or any type of object.
mlist=[letter for  letter in 'world' ]
print(mlist)



#find the square root of the given range use '**' for squaring the  number. 
mlist=[num**2 for num in range(0,10)]
print(mlist)



#square number which is even in the given range
newlist=[num**2 for num in range(0,10) if num%2==0]
print(newlist)


"""sam@sam:~/Desktop$ python append.py
['h', 'e', 'l', 'l', 'o']
['w', 'o', 'r', 'l', 'd']
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 4, 16, 36, 64]"""

