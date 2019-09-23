

import json
import csv



def loadFile(fileName,currentList):
    with open(fileName) as f:
        data = json.load(f)
        currentList = currentList.update(data)
        print(f"Loaded {len(data)} lines in {fileName}")



def getItemPrice(itemName,itemInfoList):
    if itemName=="":
        return 0
    return itemInfoList[itemName]["chaosValue"]
    # match = next((for item in itemInfoList if item["name"]=itemName))
    # match["Value"] 

def getItemProfitFated(elem):
    return elem[7]
def getItemProfitProphecy(elem):
    return elem[4]

def getItemProfitVendorRecipe(elem):
    return elem[4]

def computeFatedItem(csvName,itemInfoList):
    with open(csvName, 'r') as f:
        reader = csv.reader(f)
        fated = list(reader)
        fated.pop(0)
        
    for recipe in fated:
        # recipe["Prophecy price"]=getItemPrice(recipe["name"],itemInfoList)
        recipe.append(getItemPrice(recipe[0],itemInfoList))
        recipe.append(getItemPrice(recipe[1],itemInfoList))
        recipe.append(recipe[3]+recipe[4])
        recipe.append(getItemPrice(recipe[2],itemInfoList))
        recipe.append(recipe[6]-recipe[3]-recipe[4])

    fated.sort(key=getItemProfitFated,reverse=True)
    print("Results of Fated")
    print(fated)
    
    with open(f"result{csvName}", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(fated)

def computeProphecyItem(csvName,itemInfoList):
    with open(csvName, 'r') as f:
        reader = csv.reader(f)
        prophecy = list(reader)
        prophecy.pop(0)
        
    for recipe in prophecy:
        # recipe["Prophecy price"]=getItemPrice(recipe["name"],itemInfoList)
        recipe.append(getItemPrice(recipe[0],itemInfoList))
        recipe.append(getItemPrice(recipe[1],itemInfoList))
        recipe.append(recipe[3]-recipe[2])

    prophecy.sort(key=getItemProfitProphecy,reverse=True)
    print("Results of prophecy")
    print(prophecy)
    
    with open(f"result{csvName}", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(prophecy)    


def computeVendorRecipes(csvName,itemInfoList):
    with open(csvName, 'r') as f:
        reader = csv.reader(f)
        vendorRecipes = list(reader)
        vendorRecipes.pop(0)

    recipesResult = []  
    for recipe in vendorRecipes:
        recipeElem = []
        recipeElem.append(recipe[0])
        recipeElem.append([])
        recipeElem.append(0)
        for comp in recipe[1:]:
            if comp !="":
                price = getItemPrice(comp,itemInfoList)
                recipeElem[1].append(f"{comp} ({price})") 
                recipeElem[2]+=price
        recipeElem.append(getItemPrice(recipe[0],itemInfoList))
        recipeElem.append(recipeElem[3]-recipeElem[2])
        recipesResult.append(recipeElem)

    recipesResult.sort(key=getItemProfitVendorRecipe,reverse=True)
    print("Results of vendor recipes")
    print(recipesResult)
    
    with open(f"result{csvName}", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(recipesResult)    

def main():

    itemInfoList = {}
    fileToLoad = [
        "accessory.json","armour.json","Divination.json","Essence.json","flask.json","jewel.json","prophecy.json","weapon.json","uniquemap.json"
    ]
    for file in fileToLoad:
        loadFile(file,itemInfoList)

    computeFatedItem("Fated.csv",itemInfoList)
    computeProphecyItem("prophecy.csv",itemInfoList)
    computeVendorRecipes("vendorRecipes.csv",itemInfoList)




