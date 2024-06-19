import GetSnowflakeConnection

conn = GetSnowflakeConnection.getSnowflakeConnection()
curs = conn.cursor()
sql = ("select name from  STUTI.PUBLIC.EMPLOYEE where dept = (select dept from STUTI.PUBLIC.EMPLOYEE\
       where salary=(select max(salary)from STUTI.PUBLIC.EMPLOYEE));")
curs.execute(sql)
result = curs.fetchall()
for row in result:
    print(row)
curs.close()
conn.close()
