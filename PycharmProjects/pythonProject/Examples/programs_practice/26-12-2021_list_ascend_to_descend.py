# n(n-1)/2 = 5(5-1)/2 =10
# _________________________________________
# starting: 1 4 2 5 -6
# step:4
# -6 4 2 5 1 --> 4
# ___________________________________
# sarting: -6 2 4 5 1
# -6 1 4 5 2 -->3
# _______________________________________
# sarting: -6 1 4 5 2
# -6 1 2 5 4 -->2
# ___________________________________
# starting: -6 1 2 5 4
# -6 1 2 4 5 --> 1

list_1=[1,2,9,6,-98,53,-52,23]
list_2=[]

for i in range(len(list_1)):
    for j in range(i+1,len(list_1)):
        if list_1[i]>list_1[j]:
            list_1[i],list_1[j]=list_1[j],list_1[i]
print(list_1)