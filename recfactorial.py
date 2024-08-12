def recfactorial(num):
    if num == 1:
        return 1

    return num * recfactorial(num-1)

num = int(input("Enter a number: "))
ans = recfactorial(num)

print("The Factorial is : ",ans)