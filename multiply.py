#write a function that multiply all the number in the given list.

def multiply(num):
    total=num[0]
    for x in num:
     total*=x
    return total 

res=multiply([1,2,3,-4])
print res
