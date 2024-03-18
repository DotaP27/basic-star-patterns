n = int(input("Enter the number of rows for the triangle: "))

for i in range(n):
    print(" " * (n - i) + "*" * i)
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)
