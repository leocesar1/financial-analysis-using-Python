from requests import get
from json import dumps 


def getFinantialURL(typeFinantial = "stock"):
    if typeFinantial == "stock":
        return "quote"
    elif typeFinantial == "crypto":
        return typeFinantial


def getStockData(stockCode = ["PETR4"]):
    urlBase = f"https://brapi.dev/api/{getFinantialURL()}/{'%'.join(stockCode)}?range=12mo&interval=1d&fundamental=true"
    urlResponse = get(urlBase).json()["results"]
    return urlResponse

def getStockValue(stockCode = ["PETR4"]):
    tempValue = getStockData(stockCode)
    newValue = []
    for stock in tempValue:
        stockSymbol = stock["symbol"]
        stockName = stock["longName"]
        stockValues = stock["historicalDataPrice"]
        newValue.append(
            {
                "name": stockName,
                "symbol": stockSymbol,
                "values": stockValues
            }
            )

    return newValue

def getSpecificValue(stock = ["PETR4"], specific = "close"):
    tempValue = getStockValue(stock)
    newValue = []
    for stock in tempValue:
        specificValues = []
        for value in stock["values"]:
            specificValues.append(value[specific])

        newValue.append({
            "name": stock["name"],
            "symbol": stock["symbol"],
            specific: specificValues
            })

    return newValue

print(getSpecificValue()[0]["close"])