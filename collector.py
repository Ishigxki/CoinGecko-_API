import requests
import time 
from database import*

url = "https://api.coingecko.com/api/v3/simple/price"

params = {"ids":"bitcoin,ethereum,solana","vs_currencies":"usd"
          }



def fetch_and_store():
    response = requests.get(url,params=params)
    data = response.json()

    if response.status_code != 200:
        return("You got an error,sorry",response.status_code)
    for coin, value in data.items():
        print("Inserting:", coin, value["usd"])

        cursor.execute("INSERT INTO crypto_prices (coin,price) VALUES (%s, %s);",
                (coin, value["usd"]))
    connection.commit()
    print("Data stored successfully")
while True:
    fetch_and_store()
    time.sleep(60)