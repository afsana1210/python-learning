celcius=[0,12,35.8]

fehrenheit=[((9/5)*temp +32) for temp in celcius]
print(fehrenheit)


"""sam@sam:~/Desktop$ python celcius.py
[32, 44, 67.8]"""


fehrenheit=[]

for temp in celcius:
  fehrenheit.append((9/5)*temp +32)
  #i got same result as above.
"""sam@sam:~/Desktop$ python celcius.py
[32, 44, 67.8]"""



mylist=[x if x%2==0 else 'ODD' for x in range(0,10) ]
print(mylist)

#[0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD']


mylist=[]

for x in [1,2,3]:
 for y in [1,10,1000]:
   mylist.append(x*y)


print(mylist)
#[1, 10, 1000, 2, 20, 2000, 3, 30, 3000]


mylist=[x*y for x in [1,2,3] for y in [1,10,1000]]
print(mylist)

#we got same answer
#[1, 10, 1000, 2, 20, 2000, 3, 30, 3000]



