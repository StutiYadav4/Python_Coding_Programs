import GetSnowflakeConnection

conn = GetSnowflakeConnection.getSnowflakeConnection()
curs = conn.cursor()
sql = ("SELECT date_of_order, c.Customer_name, COUNT(o.order_id) AS order_count\
        FROM STUTI.PUBLIC.CUSTOMER c JOIN STUTI.PUBLIC.ORDER1 o ON c.customer_id = o.customer_id\
        GROUP BY date_of_order, c.Customer_name\
        ORDER BY date_of_order, order_count desc ;")
curs.execute(sql)
result = curs.fetchall()
for row in result:
    print(row)
curs.close()
conn.close()