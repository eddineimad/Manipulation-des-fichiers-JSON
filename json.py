import json  

with open("data.json", "r") as file:
    data = json.load(file)  
    print(data)  

data["langage"] = "Python"

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)  

with open("data.json", "r") as file:
    data = json.load(file)  
    print("\nContenu du fichier après modification :")
    print(data)  