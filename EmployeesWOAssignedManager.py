import GetSnowflakeConnection

conn = GetSnowflakeConnection.getSnowflakeConnection()
curs = conn.cursor()
sql = ("select * from STUTI.PUBLIC.EMPLOYEE where manager='NULL';")
curs.execute(sql)
result = curs.fetchall()
for row in result:
    print(row)
curs.close()
conn.close()




#Create database STUTI
#Use database STUTI
#"Create table Employee(Emp_no int primary key, Name varchar(20), Manager varchar(20), Age int);"
