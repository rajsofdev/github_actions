# n = int(input("Enter the number: "))
# for i in range(n):
#     for b in range(n):
#         print(f"{n}", end=" ")
#     print("\n")

#n = int(input("Enter the number to print Char: "))

for i in range(6):
    for b in range(6-i):
        print(" ",end="")
    for c in range(i):
        print(" *", end="")
    print("\n")


