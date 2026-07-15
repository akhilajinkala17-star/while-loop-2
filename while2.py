
#1.
n=1
while n<100:
    print(n)
    n+=1
# 2.
n=1
while n<6:
    print(n)
    n+=1
# 3.
n=1
while n<101:
    if n%2==0:
        print(n)
    n+=1
# 4.
n=1
while n<101:
    if n%2!=0:
        print(n)
    n+=1
# 5.
n=int(input("enter number:"))
s=1
sum=0
while s<n:
    sum=sum+s
    s=s+1
print(sum)
# 6.
n=5
fact=1
while n>=1:
    fact=fact*n
    n=n-1
print(fact)
# 7.
n=123
reverse=0
while n>0:
    digit=n%10
    n=n//10
    reverse=reverse*10+digit
print(reverse)
# 8.
n=121
temp=n
reverse=0
while n>0:
    digit=n%10
    n=n//10
    reverse=reverse*10+digit
if reverse==temp:
    print("palindrome")
else:
    print("not palindrome")
 
# 9.
n=1234
count=0
while n>0:
    digit=n%10
    n=n//10
    count=count+1
print(count)
# 10.
n = 12345
sum = 0
while n > 0:
    digit = n % 10
    n = n // 10
    sum = sum + digit
print(sum)








