def count(list):
    if len(list) == 1:
        if list[0] < 1:
            return 1
        else:
            return 0
    else:
        if list[0] < 1:
            return 1 + count(list[1:])
        else:
            return count(list[1:])


print("n = ", count([-2, 3, -8, -11, -4, 6]))
