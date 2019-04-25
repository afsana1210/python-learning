#SPY GAME-Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):

  code=[0,0,7,'x']
  #check [0,7,'x'] x is some string
  # [7,'x']
  # ['x'] len is 1. 
  for num in nums:
    if num == code[0]:
       code.pop(0)
  return len(code) == 1     


res=spy_game([1,0,2,3,0,7,8,9])
print res
