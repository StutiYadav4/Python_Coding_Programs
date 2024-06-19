import re

def read_propFile(filepath):
    properties = {}
    file = open(filepath, 'r')
    for line in file:
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            key, value = line.split('=', 1)
            properties[key.strip()] = value.strip()
    return properties

def replace_in_sql(sql_filepath, properties):
    file = open(sql_filepath, "r")
    opSql = file.read()
    def replace_match(match):
        var_name = match.group(1) or match.group(2)
        return properties.get(var_name)
    opSql = re.sub(r'\$([A-Za-z0-9_]+)|\$\{([A-Za-z0-9_]+)\}', replace_match, opSql)
    return opSql


properties = read_propFile('config.properties')
outPut = replace_in_sql('ReadFromSql.sql', properties)
print(outPut)


