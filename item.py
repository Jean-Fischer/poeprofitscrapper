
class ItemInfo(object):
    name:""
    price:0.0








class RecipeInfo(object):
    result:ItemInfo
    components : [ItemInfo]

    def getProfit(self):
        cost = 0
        for comp in self.components:
            cost += comp.price


