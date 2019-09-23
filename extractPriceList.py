
import requests
import json
import json
import sys


def extractItemList(url,fileName):
    response = requests.post(url)

    json_data = json.loads(response.text)

    itemList ={}
    for line in (json_data["lines"]):
        # itemList.append({"name":line["name"],"chaosValue":line["chaosValue"]})
        itemList[line["name"]]={"chaosValue":line["chaosValue"]}

    #print(itemList)
    print(f"Succesfully loaded {len(itemList)} items")

    with open(fileName,'w') as f :
        json.dump(itemList,f)


def main(league):


    if league=="":
        print ("No league named passed as argument. Defaulting to Standard")
        league = "Standard"
    else:
        print(f"League selected : {league}")


    print(f"Starting extraction of item prices for league {league}")
    jobList = [
    {"url":f"https://poe.ninja/api/Data/GetDivinationCardsOverview?league={league}","fileName":"Divination.json"},
    {"url":f"https://poe.ninja/api/Data/GetEssenceOverview?league={league}","fileName":"Essence.json"},
    {"url":f"https://poe.ninja/api/Data/GetMapOverview?league={league}","fileName":"map.json"},
    {"url":f"https://poe.ninja/api/Data/GetUniqueArmourOverview?league={league}","fileName":"armour.json"},
    {"url":f"https://poe.ninja/api/Data/GetUniqueFlaskOverview?league={league}","fileName":"flask.json"},
    {"url":f"https://poe.ninja/api/Data/GetUniqueWeaponOverview?league={league}","fileName":"weapon.json"},
    {"url":f"https://poe.ninja/api/Data/GetUniqueAccessoryOverview?league={league}","fileName":"accessory.json"},
    {"url":f"https://poe.ninja/api/Data/GetUniqueJewelOverview?league={league}","fileName":"jewel.json"},
    {"url":f"https://poe.ninja/api/Data/GetProphecyOverview?league={league}","fileName":"prophecy.json"},
    {"url":f"https://poe.ninja/api/Data/GetUniqueMapOverview?league={league}","fileName":"uniquemap.json"},
    ]

    for job in jobList : 
        extractItemList(job["url"],job["fileName"])


