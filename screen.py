import styvio

tickerArray = ["DAL", "LUV", "SAVE", "TXN", "AMD", "NVDA", "AAPL", "MSFT", "TSLA", "FB", "OKTA", "CRWD", "AMZN"]
ratingArray = []
buyTickers = []

for i in range(0, len(tickerArray)):
    out = styvio.get_data(tickerArray[i])["yearlyPrices"]

    print("Rating stock " + str(i + 1) + " out of " + str(len(tickerArray)))

    first = out[0]
    last = out[(len(out)-1)]

    ret = (((last)-(first))/(first)) * 100

    ratingVar = "F"

    if (ret > 100):
        ratingVar = "A+"
        buyTickers.append(tickerArray[i])
    elif (ret > 95):
        ratingVar = "A"
        buyTickers.append(tickerArray[i])
    elif (ret > 90):
        ratingVar = "A-"
        buyTickers.append(tickerArray[i])
    elif (ret > 85):
        ratingVar = "B+"
    elif (ret > 80):
        ratingVar = "B"
    elif (ret > 75):
        ratingVar = "C+"
    elif (ret > 70):
        ratingVar = "C"
    elif (ret > 65):
        ratingVar = "D+"
    elif (ret > 60):
        ratingVar = "D"
    elif (ret > 55):
        ratingVar = "F+"

    ratingArray.append(ratingVar)

print("All data")
print(tickerArray)
print(ratingArray)
print()
print("Buy these stocks:")
print(buyTickers)
