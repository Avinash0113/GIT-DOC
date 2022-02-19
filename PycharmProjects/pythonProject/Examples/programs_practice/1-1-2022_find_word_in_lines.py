

f= open("findin_lines","r")
data = f.read()
content=str(data)
print(str(data))
lines=content.split("\n")
print(lines)
print("---------------------------------------")
# data.split("\n")
# print(data)
for line in range(1,len(lines)):
    if "micron" in lines[line]:
        print(f"micron word is in line:{line}")
