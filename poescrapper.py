from extractPriceList import main as extractPriceList
from computePrices import main as computePrices
import sys


if(len(sys.argv)==1):
    extractPriceList("")
else:
    extractPriceList(sys.argv[2])

computePrices()
