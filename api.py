from database import *
from fastapi import FastAPI


app = FastAPI()
@app.get("/latest")
@app.get("/history/{coin}")
@app.get("/latest/{coin}")

def get_latest_coin(coin:str):
    cursor.execute(
        """
        SELECT coin, price, timestamp
        FROM crypto_prices
        WHERE coin = %s
        ORDER BY timestamp DESC
        LIMIT  1;

        """,(coin,))
    
    row = cursor.fetchone()

    if row is None:
        return {"error":"Coin not found"}
    
    return {
        "coin": row[0],
        "price": row[1],
         "timestamp": str(row[2])
    }
    


def get_latest():
    cursor.execute(""" SELECT DISTINCT ON (coin) coin, price, timestamp 
                   FROM crypto_prices
                   ORDER BY coin,timestamp DESC;""")
    
    rows = cursor.fetchall()

    return rows

def get_history(coin,str):
    cursor.execute("""
SELECT coin, price, timestamp
                   FROM crypto_prices
                   where coin =%s
                   ORDER BY timestamp DESC""",(coin,))
    
    rows =cursor.fetchall()

    result = []

    for row in rows:
        result.append({
            "coin": row[0],
            "price":row[1],
            "timestamp": str(row[2])
        })

    return {"data":result}