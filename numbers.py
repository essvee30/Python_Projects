n = int(input("Enter n = "))
for i in range(2,int(n/2)+1):
    if n%i == 0:
        print("Has a prime")
        break
    else:
        print(f"{n} is a prime number")

    