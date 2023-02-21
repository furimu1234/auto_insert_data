import mysql.connector
import datetime, random, time
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    host=os.environ.get("MYSQL_HOST"),
    port=os.environ.get("MYSQL_PORT"),
    database=os.environ.get("MYSQL_DATABASE")
)
print(conn)

def insert_data():
    cur = conn.cursor()
    
    today = datetime.date.today()
    now = datetime.datetime.now().time()
    
    cur.execute(
        '''
        INSERT INTO datatbl 
            (deviceid, data, date, time)
        VALUES 
            (%s, %s, %s, %s)
    ''', (9876, random.randint(1, 200), today, now)
    )
    print(f"{today} {now}: insert")
    conn.commit()
    cur.close()


if __name__ == "__main__":
    while True:
        insert_data()
        time.sleep(60)
        



if conn is not None and conn.is_connected():
        conn.close()