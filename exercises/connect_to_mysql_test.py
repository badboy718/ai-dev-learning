import pymysql
connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    charset='utf8'
)

print(connection.get_server_info())

connection.close()