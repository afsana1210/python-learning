try:
  f=open('Line',r)
  f.write('write a test line')
except:
  print'All other exception!'
finally:
  print 'i always run'  

