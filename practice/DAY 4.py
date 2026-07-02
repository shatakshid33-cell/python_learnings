num=int(input("ENTER YOUR VALUE HERE: "))
if num==0:
    print(f'The number {num} is zero')
elif num>0:
    print(f'The number {num} is positive')
else:
    print(f'The number {num} is negative')


age=int(input("ENTER YOUR AGE HERE: "))
if age>=18:
    print(f'YOUR AGE {age} IS ELIGIBLE TO VOTE')
if age<0:
    print(f'YOUR AGE {age} IS INVALID')
else:
    print(f'YOUR AGE {age} IS NOT ELIGIBLE TO VOTE')

num1=int(input("ENTER YOUR FIRST VALUE HERE: "))
num2=int(input("ENTER YOUR SECOND VALUE HERE: "))
if num1>num2:
    print(f'The number {num1} is greater than {num2}')
elif num1<num2:
    print(f'The number {num2} is greater than {num1}')

year=int(input("ENTER YOUR YEAR HERE: "))
if year%4==0:
    print(f'The year {year} is a leap year')
else:
    print(f'The year {year} is not a leap year')

#print sum of first 20 odd natural numbers 
sum=0
for i in range(0,41,2):
    sum=sum+1
print(f'The sum of first 20 odd natural numbers is {sum}')

#print factorial of a number
num=int(input("ENTER A NUMBER HERE: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f'The factorial of {num} is {factorial}')

#how many digits
num=int(input("ENTER A NUMBER HERE: "))
count=0
while num>0:
    num=num//10
    count=count+1
print(f'The number of digits in the number is {count}')

num=input("ENTER A NUMBER HERE: ")
print(f' THE LENGTH OF THE NUMBER IS {len(num)}')

#ADD DIGITS
num=int(input("ENTER A NUMBER HERE: "))
sum=0
for i in str(num):
    sum=sum+int(i)
print(f'The sum of the digits of {num} is {sum}')


word=input("ENTER A WORD HERE: ")
count=0
for i in word:
    if i=="a":
        count=count+1
    elif i=="e":
        count=count+1
    elif i=="i":
        count=count+1
    elif i=="o":
        count=count+1
    elif i=="u":
        count=count+1
print(f'The number of vowels in the word "{word}" is {count}')
