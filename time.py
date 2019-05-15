import datetime
t=datetime.time(5,25,1)
print t
#print minimum time using min attribute
print datetime.time.min
#print maximum time using max attribute
print datetime.time.max
print datetime.time.resolution
#print using date class with today attribute
today=datetime.date.today()
print today
#timetuple struct will give you different aspect and atrribute information
print today.timetuple()
#saperately print year,month and day 
print today.year
print today.month
print today.day
#print minumum date
print datetime.date.min
#print max date
print datetime.date.max
#print resolution
print datetime.date.resolution
d1=datetime.date(2019,5,15)#05 will give you error u should write 5 only
print d1
#replace the d1 time using replace method
d2=d1.replace(year=1998)
print d2