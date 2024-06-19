#part 1

import GetSnowflakeConnection

conn = GetSnowflakeConnection.getSnowflakeConnection()
curs = conn.cursor()
sql = ("SELECT Maker, MIN(Price) AS MinPrice, MAX(Price) AS MaxPrice\
        FROM STUTI.PUBLIC.Car_data\
        GROUP BY Maker\
        ORDER BY Maker;")
curs.execute(sql)
result = curs.fetchall()
for row in result:
    print(row)
curs.close()
conn.close()