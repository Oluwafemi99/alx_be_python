size = int(input("Enter the size of the pattern:"))
rows = 1
while rows <= size:
    cols = 1
    while cols <= size:
        print("*", end="")
        cols += 1
    print()
    rows += 1