def fizzbuzz():
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz", end=' ')
        else if num % 3 == 0:
            print("{num}". format(num = "Fizz"), end=' ')
        elif num % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(num, end=' ')
