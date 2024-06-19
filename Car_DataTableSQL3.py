#part 3

import GetSnowflakeConnection

conn = GetSnowflakeConnection.getSnowflakeConnection()
curs = conn.cursor()
sql = ("SELECT *\
        FROM STUTI.PUBLIC.Car_data c\
        JOIN (\
        SELECT Type, MAX(Horsepower) AS MaxHorsepower\
        FROM STUTI.PUBLIC.Car_data\
        GROUP BY Type\
        )m  ON c.Type = m.Type AND c.Horsepower = m.MaxHorsepower;")
curs.execute(sql)
result = curs.fetchall()
for row in result:
    print(row)
curs.close()
conn.close()