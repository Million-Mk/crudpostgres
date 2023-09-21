import psycopg2
# สร้าง fn สำหรับเชื่อมต่อฐานข้อมูล postgreSQL 
def connectdb():
    connection = psycopg2.connect(
        host="localhost",
        database="sampledb",
        user="postgres",
        password="1234",
        port=5432
    )
    return connection 

# ทดสอบเรียกใช้งาน fn 

print(connectdb())