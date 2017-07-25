print "Design and develop an algorithm for evaluating the polynomial f(x)  = a4x4 + a3x3 + a2x2 + a1x + a0,"
print "for a given value of x and its coefficients using Horner's method. Implement a Python program for "
print "the same and execute the program for different sets of values of coefficients and x."

a=[]
n=input("\nenter number of coefficients:")
print "enter coefficients:"
i=1
for i in range(0,n):
    a.append(input())

x=input("enter value of x:")
sum=0
while i>0:
    sum=(sum+a[i])*x
    i-=1
sum=sum+a[0]
print "sum is:",sum
