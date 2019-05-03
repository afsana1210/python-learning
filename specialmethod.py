class Book():

  def __init__(self,title,author,page):
    self.title=title
    self.author=author
    self.page=page
  
  #special method
  def __str__(self):
   return  self.title+self.author

  def __len__(self):
    return self.page 

  def __del__(self):
    print 'a book object has been deleted'  

b=Book('python book',' tom ',200)
print b 


print len(b)

del b