from database import *
from fastapi import FastAPI


app = FastAPI()
@app.get("/latest")


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
            "timestamp": str(rows[2])
        })

    return {"data":result}