#regular expression
import re
split_term='@'

phrase='what is your emial,is it hello@gmail.com'
print re.split(split_term,phrase)
#findall method find the all instance of given pattern
print re.findall('match','here is on match, here is another match')


