with open("file2","r") as b:
    with open ("file1","r") as f:
        data= f.readlines()
        data_1= b.readlines()
        print(data,data_1)

        for char in data:
            if "[FAIL]" in char:
                print(char)
        for element in data_1:
            if "[FAIL]" in element:
                print(element)
        else:
            print("no error")
# {File1.txt:"[FAIL]: This is Firmware failure", File2.txt:"No_error"}










