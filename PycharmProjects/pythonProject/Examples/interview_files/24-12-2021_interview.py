
student = ["raviteja","bharath","avinash","anjayya","mahesh","ganesh","visu","sumanth"]

#print(student,end="\n")

# for index in student:
#     print(index)
for index in range(0,len(student)):
    print(index,student[index])
    if student[index]=="mahesh":
        #mahesh_place=index
        print(f"....{index} is {student[index]}")
        print(f"....{index-1} is {student[index-1]}")
        print(f"....{index+1} is {student[index+1]}")
