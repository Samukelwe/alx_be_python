# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end="")
        col += 1
    print()
    row += 1