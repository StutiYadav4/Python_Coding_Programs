# So you need not write this again and again.
'''import jaydebeapi

conn = jaydebeapi.connect("com.snowflake.client.jdbc.SnowflakeDriver",
                         "jdbc:snowflake://io78130.ap-southeast-1.snowflakecomputing.com",
                          ["STUTIYADAV4", "Lecture04"],
                          "C:\\Users\\Stuti Yadav\\Downloads\\snowflake-jdbc-2.8.0.jar")'''

import GetSnowflakeConnection
conn = GetSnowflakeConnection.getSnowflakeConnection()

curs = conn.cursor()
curs.execute("select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER Limit 5;")
result = curs.fetchall()
for row in result:
    print(row)
curs.close()
conn.close()



