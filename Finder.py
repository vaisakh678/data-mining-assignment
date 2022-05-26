def find(_x, _y, offset=0):
    for _ in range(offset):
        # print(' ', end="")
        print(end=" ")
    for x, y in zip(_x, _y):
        if (x != y):
            print("^", end=" ")
        else:
            print(" ", end=" ")