print "\n Python program to reverse a given integer number and check whether it is a"
print "PALINDROME or not. Output the given number with suitable message\n\n"
num=input("Enter a valid integer number:")
temp = num
rev=0
while(num != 0):
    digit=num % 10
    rev=rev * 10 + digit
    num=num / 10
print "\n\n The reversed number",rev

if(temp == rev):
    print "\n The number is PALINDROME\n"
else:
    print "\n The number is not PALINDROME\n"
