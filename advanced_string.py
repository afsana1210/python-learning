#advanced string
s='hello world'
print s.capitalize()
u=s.upper()
print u
l=s.lower()
print l
print s.count('o')
print s.find('o')
print s.endswith('d') 
print s.center(20,'z')
t='this is tab\t example'.expandtabs()
print t 
st='hello'
print st.isupper() 
print st.isalnum()
print st.isalpha()
print st.islower()
print st.isspace()
print st.istitle()
i=st[-1]=='o'
print i  
sp=st.split('e')    #splits every instance
print sp
pt='hihiihiihiihhhhi'
p=pt.partition('i') #split first instance of string
print p