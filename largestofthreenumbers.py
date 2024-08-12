num1 = input("Enter the First Number : ")
num2 = input("Enter the Second Number : ")
num3 = input("Enter the Third Number : ")

if num1 > num2:
    if num1 > num3:
        max = num1
    else:
        max = num3
else:
    if num2 > num3:
        max = num2
    else:
        max = num3

print("The Largest of Three Numbers is : ",max)