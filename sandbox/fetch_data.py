from binance.client import Client

# Fetch crypto historical data and write to file for training
with open('keyfile.conf', "r") as keyfile:
    KEYS = keyfile.read().splitlines()

client = Client(KEYS[0], KEYS[1])
klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2005")

# Add header, convert to int, write to csv
with open('dataset.csv', 'w+') as f:
    header_str = "Open time,Open,High,Low,Close,Volume,Close time,Quote asset volume,Nr of trades,Taker buy base asset volume,Taker buy quote asset volume"
    f.write('%s\n' % header_str)
    for items in klines:
        del items[-1] # rm last column
        items_str = ','.join(map(str, items))
        f.write('%s\n' % items_str)
    print("File written")
