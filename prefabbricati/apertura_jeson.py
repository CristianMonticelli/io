import json
Nome = {}
Nome = []
FILE_PATH = "Nome.json"  
try:
    with open(FILE_PATH, 'r') as file:
        Nome = json.load(file)
except FileNotFoundError:
    pass