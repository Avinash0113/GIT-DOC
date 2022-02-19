"""
    1    row = 0, row-1 = -1 range(-1,-1,-1) = []
   12 1  row = 1  row-1 = 0 range(0,-1,-1) = [0]
  123 21  row = 2 row-1=1 range(1,-1,-1) = [1 0]
 1234 321
12345 4321
n = 5
"""
""" 
        *
       * *
      * * *
     * * * *
    * * * * *
"""
rows = 5
for row in range(rows):
    print(" "*(rows-row-1),end=" ")
    print("*",end=" ")