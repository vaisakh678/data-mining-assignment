def find(_x, _y, offset):
    for i in range(offset):
        print(' ', end="")
    for x, y in zip(_x, _y):
        if (x != y):
            print("^", end=" ")
        else:
            print(" ", end=" ")