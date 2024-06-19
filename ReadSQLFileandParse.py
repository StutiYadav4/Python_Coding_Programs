import GetSnowflakeConnection
import csv
import re
import threading

def read_conFile(filepath):
    fileout = {}
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, value = line.split('=', 1)
                fileout[key.strip()] = value.strip()
    return fileout

def replace_in_sql(sql_filepath, properties):
    with open(sql_filepath, "r") as file:
        opSql = file.read()
        def replace_match(match):
            var_name = match.group(1)
            return properties.get(var_name, f"${{{var_name}}}")
        opSql = re.sub(r'\$([A-Za-z0-9_]+)', replace_match, opSql)
    return opSql

def execute_queries(conn, queries):
    with open("query_results.csv", "w", newline="") as fileout:
        writer = csv.writer(fileout)
        writer.writerow(["Query""\t\t\t\t""Status""\t\t\t\t""Failure Reason"])
        for query in queries:
            query = query.strip()
            if query:
                t1 = threading.Thread(query_, conn, query)
                status, failure_reason = query_(conn, query)
                writer.writerow([query, status, failure_reason])


def query_(conn, query):
    try:
        curs = conn.cursor()
        curs.execute(query)
        return "Success", ""
    except Exception as e:
        return "Failure", str(e)


if __name__ == "__main__":
    conn = None
    try:
        conn = GetSnowflakeConnection.getSnowflakeConnection()
        properties = read_conFile('PythonConstantFile.py')
        modified_sql = replace_in_sql('ReadFromSQL1.sql', properties)
        print(modified_sql)

        execute_queries(conn, modified_sql.split(';'))
        print("Execution completed. Check query_results.csv for the report.")
    except Exception as main_e:
        print(f"An error occurred: {main_e}")
    finally:
        if conn:
            conn.close()


