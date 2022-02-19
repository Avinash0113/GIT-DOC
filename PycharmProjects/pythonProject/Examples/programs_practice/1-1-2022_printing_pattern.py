input_rows = int(input("Enter required rows?"))
star = "* "
space = "  "

for row in range(1,input_rows+1):
    #print(row)
    print((input_rows-row)*space, end="")
    print((2*row-1)*star, end="")
    print((input_rows - row) * space, end="")
    print()
