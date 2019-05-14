from collection import namedtuple
cat=namedtuple('cat',fur claws name)
c=cat(fur='fuzzy',claws=False,name='kitty')
print c
#attribute call
print c.name
#used index
print c[2]