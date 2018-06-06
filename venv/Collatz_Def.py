import sys

def number(num):
    while num > 1:
        if num % 2 == 0:
            num = num/2
            print(int(num))
        else:
            num = num*3+1
            print(int(num))

num = int(input ("Please choose your number: "))

number(num)
print(number(num))



