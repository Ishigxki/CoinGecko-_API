from database import connection, cursor

def test_db():
    try:
        cursor.execute("SELECT * FROM crypto_prices;")
        rows = cursor.fetchall()
        print("Connection successful:", rows)
    except Exception as e:
        print("Error:", e)



test_db()