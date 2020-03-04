def coprime(a, b):
    if b == a:
        return False
    if a > b:
        a, b = b, a

    divisors = []
    for i in range(2, a):
        if a % i == 0:
            divisors.append(i)

    for divisor in divisors:
        if b % divisor == 0:
            return False

    return True

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
if coprime(a, b):
    print(str(a) + " and " + str(b) + " are coprime!")
else:
    print(str(a) + " and " + str(b) + " are not coprime.")
