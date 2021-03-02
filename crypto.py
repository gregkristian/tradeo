import sys
import pprint
from binance.client import Client
from matplotlib import pyplot as plt

# Get arg for key file
if (len(sys.argv) != 2):
    sys.exit('Error: wrong number of arg. Expect 1 for key')
else:
    keyfile = sys.argv[1]

with open(keyfile, "r") as file:
    KEYS = file.read().splitlines()

client = Client(KEYS[0], KEYS[1])

klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 day ago UTC") # 60m * 24h = 1440 klines

close_price = [int(float(el[4])) for el in klines] # get 4th element (close price) from each kline. Ignore the cents

plt.plot(close_price)
plt.savefig("plot.png")

