

class Collatz(object):

    def __init__(self, num):
        self.num = num

    def output(self):
        num = self.num
        while num > 1:
            if num % 2 == 0:
                num = num / 2
                print(int(num))
            else:
                num = num * 3 + 1
                print(int(num))

num = int(input ("Please choose your number: "))
num = Collatz(num)
print(num.output())