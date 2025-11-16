import oracledb

connection_string = '''(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.ap-hyderabad-1.oraclecloud.com))(connect_data=(service_name=g21bd6f153efbd1_atp23_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))'''

conn = oracledb.connect(user="admin", password="Welcome@1234@", dsn=connection_string)

cursor = conn.cursor()
cursor.execute("SELECT * FROM all_tables where rownum = 1")
for row in cursor:
    print(row)
conn.close()