def chck_even(num):
 return num % 2 == 0

mylist=[1,2,3,4,5,6,7,8,9]

res=filter(chck_even,mylist)
print res