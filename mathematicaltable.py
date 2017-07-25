def table(n):
        for j in range(1,num+1):
            for i in range(1,11):
                print str(j)+"X"+str(i)+"="+str(j*i)
            print "\n"
            
num=input("enter the value:")
table(num)
