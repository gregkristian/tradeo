import os
from binance.client import Client

def get_keys():
    try:
        KEYS=(os.environ['BINANCE_API_KEY'], os.environ['BINANCE_SECRET'])
        return KEYS
    except:
        print("Error fetching API keys")
        #exit?

def get_client():
    KEYS = get_keys()
    client = Client(KEYS[0], KEYS[1])
    return client

client = get_client()
order = client.create_order(
    symbol='BTCUSDT',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)


