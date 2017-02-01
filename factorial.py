"""Factorial of any number between 0 to 989 using recursive function"""

num=int(input("enter a integer number:"))

def fact(f):
	"this function computes factorial" #optional function description
	if f==0:
		return 1
	else:
		return f*fact(f-1)

"""res=fact(num)
print res

"""
i=0
while(i<=num):

	res=fact(i)
	print "Factorial("+str(i)+")="+str(res)
	i=i+1
	
