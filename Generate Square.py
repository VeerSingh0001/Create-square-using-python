sizeofsq = int(input("Enter size of square: "))
spch = input("Enter spacial character which you want to use for creating square: ")
a = 1
while a <= sizeofsq:
    if a == 1 or a == sizeofsq:
        b = 1
        while b <= sizeofsq:
            print(spch, "  ", end="")
            b += 1
    else:
        b = 1
        while b <= sizeofsq:
            if b == 1 or b == sizeofsq:
                print(spch, "  ", end="")
                b += 1
            else:
                print("    ", end="")
                b += 1
    a += 1
    print()
