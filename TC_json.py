import json

data ={
    "name" :"Rohith",
    "age" : 24,
    "Skills" :["Python","java"]
}

with open("data.json","w") as file:
    json.dump(data,file,indent= 4)