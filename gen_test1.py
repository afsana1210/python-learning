def gen_square(n):

 for i in range(n):
   yield i**2

for num in gen_square(10):
   print num  