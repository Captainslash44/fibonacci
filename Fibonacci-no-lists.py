n = int(input("Enter and integer: "))

number_one = 0
number_two = 1

answer = "0,1"

if n <= 0:
    print("Invalid")
elif n == 1:
    print(number_one)
elif n == 2:
    print(f"{number_one}, {number_two}")
else:
    for i in range(n-2): # (n-2) because the first 2 numbers are already known
        total = number_one + number_two
        answer += "," + str(total)
        number_one = number_two
        number_two = total
    print(answer)
