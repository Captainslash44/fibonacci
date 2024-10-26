n = int(input("Enter and integer: "))

numbers = [0,1]
if n < 0:
    print("???")
elif n == 0:
    print("How am I supposed to print 0 numbers?")
elif n == 1:
    print("0")
elif n == 2:
    print("0,1")
else:
    for i in range(2,n):
        numbers.append(numbers[i - 1] + numbers[i - 2])

    for i in range(len(numbers)):
        print(numbers[i],end=" ")