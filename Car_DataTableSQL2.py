#part 2

import GetSnowflakeConnection

conn = GetSnowflakeConnection.getSnowflakeConnection()
curs = conn.cursor()
sql = ("select * from STUTI.PUBLIC.Car_data where length*breadth*height = (select max(length*breadth*height)\
       from STUTI.PUBLIC.Car_data ) ;")
curs.execute(sql)
result = curs.fetchall()
for row in result:
    print(row)
curs.close()
conn.close()


