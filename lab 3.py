# 70pt
def printMax(num, num1):
    if num > num1:
        print num
    else:
        print num1

# 80 pt 
def printMaxMin(num, num1, num2):
    # maximum
    if num > num1 and num > num2:
        print num
    elif num1 > num and num1 > num2:
        print num1
    elif num2 > num and num2 > num1:
        print num2
    # minimum
    if num < num1 and num < num2:
        print num
    elif num1 < num and num1 < num2:
        print num1
    elif num2 < num and num2 < num1:
        print num2
        
# 90 pt
def isEvenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"