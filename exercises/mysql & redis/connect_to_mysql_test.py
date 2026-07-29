import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='my_db',
    charset='utf8'
)
cur=conn.cursor()

#row=cur.execute("insert into products values(14,'test',999,9.2,'非自营',3);")

# sql="insert into products values(%s,%s,%s,%s,%s,%s)"
# data=(14,'test',999,9.2,'非自营',3)
# row=cur.execute(sql,data)
# print(row)

# sql="update products set price=%s where id=%s"
# data=(9999,14)
# row=cur.execute(sql,data)
# print(row)

sql="delete from products where id=%s"
data=14
row=cur.execute(sql,data)
print(row)

conn.commit()

cur.close()
conn.close()