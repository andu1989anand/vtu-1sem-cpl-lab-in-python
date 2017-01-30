""" python program to Design and develop a flowchart or an algorithm that takes three coefficients (a, b, and c) of
a Quadratic equation (ax^2 +bx+c=0) as input and compute all possible roots. Implement a Python 
program for the developed flowchart/algorithm and execute the same to output the possible
roots for a given set of coefficients with appropriate messages.find two roots of a quadratic equation """

a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
c=float(input("enter value of c:"))

disc=(b*b)-(4*a*c)

if (disc==0):
	r1=r2=-b/(2*a)
	print "roots are equal:",r1
elif (disc >0):
	print "roots are not equal"
	r1=(-b+(disc**0.5))/(2*a)
	r2=(-b-(disc**0.5))/(2*a)
	print "root1:",r1
	print "root2:",r2
else:
	print "roots are imaginary"
	r=-b/(2*a)
	i1=(abs(disc)**0.5)/(2*a)
	i2=(abs(disc)**0.5)/(2*a)
	print "root1:"+str(r)+"+i"+str(i1)
	print "root2:"+str(r)+"-i"+str(i2)
