def ask_for_input():
  
   while True:
     try:
       result=int(input('please provide number'))
       
    #if number is not provided,then except block will be run and again goes to try block thts why continue keyword is used here, 
     except:
        print'that is not a number'
        continue
    #if no except or no error then control goes to else and break the else block and goes out of the while loop. 
     else:
       print 'yes,thank you'
       break
     finally:
       print 'end of try/except'   

ask_for_input()        