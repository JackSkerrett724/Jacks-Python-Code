import math

while True:
    ps = reversed(range(1, 10000000))
    number = 0

    number = int(input("What radical do you want to simplify: "))

    for i in ps:
        i = i * i
        attempt = number/i
        if attempt == int(attempt):
            print(i, attempt)
            num1 = i
            num2 = attempt
            break

    num1 = math.sqrt(num1)
    print(num1,"√",num2)

