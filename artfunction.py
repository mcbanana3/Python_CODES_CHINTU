def sumfunction(num1, num2):
    return num1 + num2

def subfunction(num1, num2):
    return num1 - num2

def multifunction(num1, num2):
    return num1 * num2

def dividefunction(num1, num2):
    return num1 / num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = sumfunction(num1, num2)
sub = subfunction(num1, num2)
mul = multifunction(num1, num2)
quo = dividefunction(num1, num2)

print("The sum is", sum)
print("The sub is", sub)
print("The mul is", mul)
print("The div is", quo)