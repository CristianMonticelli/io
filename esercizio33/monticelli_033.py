import json
with open("esercizio33.json", "r") as file_json:
    try:        
        mylist = json.load(file_json)    
    except:        
        mylist = []
print(type(mylist))
print(mylist)
        
#mylist.append({"id":"Pezzolesi",
#            "importo":128.54,
#            "sconto_fattura":15})
#
#with open("esercizio33.json","w") as file_json:
#    json.dump(mylist,file_json,indent = 4)