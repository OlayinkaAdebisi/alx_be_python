size = int(input("Enter the size of the pattern: "))
if size >= 1:
    i = 0
    while i < size:
        for x in range(size):
            print("*", end="")
        print(i)
        i += 1