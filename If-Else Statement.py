#zero number take
n = int(input("Enter a number: "))
if n == 0:
    print("The number is zero.")
else:
    print("The number is non-zero.")


#Larger number
a=int(input("Enter First a Number"))
b=int(input("Enter the second Number"))
if(a>b):
    print("a is grater than b")
else:
    print("b is greater than a")

#Positive Or negative number
n = int(input("Enter a number: "))
if n > 0:
    print("The number is positive.")
elif n < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#check vowel or constant
ch = input("Enter a character: ")

if ch in 'aeiou':
    print("It is a vowel.")
else : 
    print("It is the Constant.")



# Student Performance Evalution
percentage=float(input("Enter the Percentage" ))

if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Poor performance")


#Largest of three number

a=int(inut("Enter the first number"))
b=int(input("Enter the second Number"))
c=int(input("Enter the third number"))
if(a>b & a>c):
    print("a is greater than b and c")
elif(b>a & b>c):
    print("b is greater than a and c")
else:
    print("c is greater")
    
# smallest of three number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number is: {a}")
elif b <= a and b <= c:
    print("Smallest number is: {b}")
else:
    print("Smallest number is: {c}")


#Natural number upto n
n = int(input("Enter value of n: "))
i = 1
while i <= n:
    print(i)
    i += 1 # i=i+1

    
#  Even number
if n%2==0:
    print("This is the even number")
while i<=n:
 print (i)
 i=i+2


#odd number
n = int(input("Enter value of n: "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 2


#natural number
n = int(input("Enter the number"))
i=1
sum =0
while i<=n:
    sum=sum+1
    i=i+1
    print(sum)

#  sum of odd number
i=1
sum=0
while i<=n:
    sum=sum+1
    i=i+2
    print(sum)

# sum of even number 
n=int(input("Enter the value of n : "))   
i=2
sum=0
while i<=n:
    sum=sum+i
    i=i+2
    print(sum)

# in reverse order natural number
n=int(input("Enter the value of n : ") )  
i=1
while i<=n:
    print(n)
    n=n-1

#Fibonacci series up to n
n = int(input("Enter number of terms: "))
a, b = 0, 1
i = 0
while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1

#Factorial of number
n=int(input("Enter the value of n : "))
i=1
fact=1
while i<=n:
    fact=fact*i
    print(fact)
    i=i+1


#check prime number or not

n = int(input("Enter a number: "))
i = 2
is_prime = True

if n <= 1:
    is_prime = False
else:
    while i <= n // 2:
        if n % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(n, "is a Prime number.")
else:
    print(n, "is not a Prime number.")

# sum of digits given number
n=int(input("Enter the number"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
    print(sum)

    #check number is Palindrome
n=int(input("Enter the number")) 
original=n 
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
    if original==reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")    

 #reverse number
num = int(input("Enter a number: "))
reverse = 0  
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

#multiplication table in while loop




