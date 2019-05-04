class Bank:
 
 def __init__(self,owner,balance=0):
   self.owner=owner
   self.balance=balance

 def deposit(self,dep_amount):
    self.amount=dep_amount
    self.balance=self.balance+dep_amount
    print 'added to the balance'.format(self.balance)

 def withdrawal(self,wt_amount):
    self.amount=wt_amount
   
    if self.balance >= wt_amount:
     print 'withdraw accepted'
    
    else:
     print 'sorry not enough funds!'

 def __str__(self):
    return 'owner:{} \nbalance:{}'.format(self.owner,self.balance)  

b=Bank('afs',1000)
print b.owner 

print b.balance

print b

b.deposit(100)


b.withdrawal(1100)