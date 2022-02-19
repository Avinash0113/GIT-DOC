import random
total_players = ["bharath","avinash","mahesh","visu","sumanth","ravi"]
dict_1={}
input_rounds=int(input("Enter number of rounds needed:"))
for i in range(1,input_rounds+1):
    for player in range(len(total_players)):
        rolling_dice=random.randint(1,6)
        if dict_1.keys()==total_players[player]:
            dict_1[total_players[player]] += rolling_dice
        else:
            dict_1[total_players[player]]=rolling_dice
print(dict_1)
