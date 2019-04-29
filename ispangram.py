import string

def ispangram(str1,alphabet=string.ascii_lowercase):
   alphaset=set(alphabet)
   return alphaset <= set(str1.lower())



res=ispangram('the quickly brown fox jumps over the lazy dog')
print res