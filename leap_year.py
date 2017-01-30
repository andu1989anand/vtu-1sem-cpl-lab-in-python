"""Design and develop a Python program to read a year as an input and find whether it is leap year
or not. Also consider end of the centuries."""

year=int(input("enter a year:"))

if (((year%4==0) or (year%100==0)) or (year%400==0)):
	print "entered year %d is a LEAP YEAR" %year
else:
 	print "entered year %d is a NOT A LEAP YEAR" %year
