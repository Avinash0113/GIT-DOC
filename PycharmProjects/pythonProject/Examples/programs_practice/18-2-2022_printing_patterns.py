
"""
*
***
*****
*******

rows=8
for row in range(1,rows,2):
    print(""*(rows-row),"*"*row,end="")
    print()
"""
"""
rows=5
for row in range(1,rows+1):
    print(" "*(rows-row),"*"*row,end="")
    print()
"""
rows=5
for row in range(1,rows+1):
    print(" "*(rows-row),end="")
    for column in range(1,row+1):
        print("*",end=" ")
    print()





















