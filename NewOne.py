def fizzbuzz(x):
    a = "fizzbuzz"
    b = "fizz"
    c = "buzz"
    while x <= 100:
        if x % 5 == 0 and x % 3 == 0:
            print(a)
        elif x % 5 == 0:
            print (b)
        elif x % 3 == 0:
            print(c)
        else:
            print(x)
        x = x + 1

fizzbuzz(50)

