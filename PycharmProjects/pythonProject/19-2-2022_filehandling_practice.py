with open (r"C:\Users\Avinash\PycharmProjects\newfile","r") as f:
    data=f.read()
    print(data)
    list_1=[]
    splitted =data.split()
    for line in splitted:
        # for word in line.split():
        #     list_1.append(splitted)
        if "python" in line:
            print(line)






