def rightstar(x):
    for i in range(1, x+1):
        print(" " * (x-i) + "$" * i)

a = int(input("Enter the row number: "))
rightstar(a)
