"""Design and develop an algorithm to find the reverse of an integer number NUM and check
whether it is PALINDROME or NOT. Implement a C program for the developed
algorithm that takes an integer number as input and output the reverse of the same with
suitable messages. Ex: Num: 2014, Reverse: 4102, Not a Palindrome"""

a=int(input("enter an interger value :"))

temp=a
rev=0
while (a>0): 
	rem=a%10
	a=a/10
	rev=rev * 10+rem
print "entered number is: %d\nreversed number is: %d" %(temp,rev)

if(temp==rev):
	print "\"%d in a PALINDROME\"" %temp
else:
	print "\"%d in a NOT A PALINDROME\"" %temp
