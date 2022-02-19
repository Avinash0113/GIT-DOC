rows=7
for row in range(rows-1):
    print(" " * (rows - (row+1)),end="")
    print("*",end="")
    if row != 0:
        print(" "*(2*(row-1)+1),end="")
        print("*",end="")
    print()
print("*"*((2*rows)-1))




