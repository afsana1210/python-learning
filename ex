def ask_for_input():
  
   while True:
     try:
       result=int(input('please provide number'))
     except:
        print'that is not a number'
        continue
     else:
       print 'yes,thank you'
      finally:
       print 'end of try/except'    