villages = [{"Name":"Village 1","Items":["Sword","Knife","Axe"],"IsSaved":False},
            {"Name":"Village 2","Items":["Potion","Food","Map"],"IsSaved":False},
            {"Name":"Village 3","Items":["Gold","Bow","Arrow"],"IsSaved":False},
            {"Name":"Village 4","Items":["Shield","Golden Apple","Helmet"],"IsSaved":False},
            {"Name":"Village 5","Items":["TNT","CrossBow","Flint"],"IsSaved":False},
            {"Name":"Village 6","Items":["Enchanted Book","Stick","Wheat"],"IsSaved":False},
            {"Name":"Village 7","Items":["Iron Ignot", "Water", "Diamond Horse Armor"],"IsSaved":False}
            ]

backpack = {}

roadMap = []

roadMap.pop(0)

def addVillageToRoadMap(village):
    
    if not village['IsSaved'] and village in villages:
        print(f"{village['Name']} has been added to roadMap.")
        roadMap.append(village)
    else:
        print(f"{village['Name']} is already saved or not in the list of villages.")
    

        
