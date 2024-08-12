start = int(input("Enter a Start number : "))
finish = int(input("Enter a Finish number : "))

for i in range(start, finish+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count = count + 1
        else:
            continue
    if count == 2:
        print(i)
    else:
        continue
