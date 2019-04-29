#write a function that check whether a number in given range(inclusive of high and low)

def chk_range(nums,low,high):
 if nums in range(low,high):
   print "%s is in the range" %str(nums)
 else:
   print "number is outside the range"


 

chk_range(3,1,9)    
