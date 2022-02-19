import json

x = {"Name":"Avinash Pamujula",
    "Father_name":"Ganeshbabu Pamujula",
    "Adhar":"73012",
    "Address":"B8-1114, Kasipalem, Buchireddy palem, Nellore"}
#with open("jason1.json", "w") as f:
y = json.loads(x)
print(y)
