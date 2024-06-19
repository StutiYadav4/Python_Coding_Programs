import GetSnowflakeConnection

conn = GetSnowflakeConnection.getSnowflakeConnection()
curs = conn.cursor()
sql = ("SELECT e.name AS manager_name\
        FROM stuti.public.emp e\
        JOIN (\
        SELECT manager_id\
        FROM stuti.public.emp\
        WHERE manager_id IS NOT NULL\
        GROUP BY manager_id\
        HAVING COUNT(id) >= 5\
        ) subquery\
        ON e.id = subquery.manager_id;")
curs.execute(sql)
result = curs.fetchall()
for row in result:
    print(row)
curs.close()
conn.close()