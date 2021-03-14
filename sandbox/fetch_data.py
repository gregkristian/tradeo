from binance.client import Client

# Fetch crypto historical data and write to file for training
with open('keyfile.conf', "r") as f1:
    KEYS = f1.read().splitlines()

client = Client(KEYS[0], KEYS[1])
klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2005")
daily_close_prices = [int(float(el[4])) for el in klines]

# Write to file
with open('trainingset.txt', 'w+') as f2:
    for items in daily_close_prices:
        f2.write('%s\n' %items)
    print("File written")
