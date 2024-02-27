import json
with open("esercizio33.json", "r") as file_json:
    try:        
        mylist = json.load(file_json)    
    except:        
        mylist = []
print(type(mylist))
print(mylist)
        
