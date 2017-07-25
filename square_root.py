print "Design and develop a flowchart to find the square root of a given number N."
print "Implement a Python program for the same and execute for all possible inputs"
print "with appropriate messages. Note Don't use library function sqrt(n) "

n=input("\nEnter the number to find the squareroot:")
if n>0:
    s = n/ 2.0;
    i=1
    while i<n :
        s = (s + (n/s))/2.0
        i+=1
    print "Square root of %f is %f" %(n,s)
else:
    print "\n Not possible to find the square root"
