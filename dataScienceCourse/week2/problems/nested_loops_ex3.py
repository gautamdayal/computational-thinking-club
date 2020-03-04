n = int(input("What is your number? "))

prime = True

for factor in range(2, n):
    if n % factor == 0:
        prime = False
        break

if prime:
    print(str(n) + " is a prime!")
else:
    print(str(n) + " is not a prime.")
