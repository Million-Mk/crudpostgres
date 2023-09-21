
# # importing sys
import sys
sys.path.insert(1, 'service')

import connectpostgres as con

print("Connect")


def insert(fullname,email,age):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "INSERT INTO person(fullname,email,age) VALUES(%s,%s,%s)"
    cursor.execute(sql,(fullname,email,age))
    conn.commit()
    cursor.close()

# fn select all data from table person
def select_all():
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "Select * from person order by id asc"
    cursor.execute(sql)
    result = cursor.fetchall()

    rows = [['ID','FullName','Email','Age','Creatdate']]
    for data in result:
        rows.append(data)
    cursor.close()
    return rows

def select_by_id(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "Select * from person where id = %s"
    cursor.execute(sql,(id,))
    result = cursor.fetchall()
    rows = [['ID','FullName','Email','Age','Creatdate']]
    for data in result:
        rows.append(data)
    cursor.close()
    return rows
    
def update_by_id(fullname,email,age,id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "Update person SET fullname = %s,email = %s,age = %s where id = %s"
    cursor.execute(sql,(fullname,email,age,id))
    conn.commit()
    cursor.close()

def delete_by_id(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "Delete from person where id = %s"
    cursor.execute(sql,(id,))
    conn.commit()
    cursor.close()