import psycopg2
# สร้าง fn สำหรับเชื่อมต่อฐานข้อมูล postgreSQL 
def connectdb():
    # connection = psycopg2.connect(
    #     host="localhost",
    #     database="sampledb",
    #     user="postgres",
    #     password="1234",
    #     port=5432
    # )

    connection = psycopg2.connect(
        host="dpg-ck5so2b6fquc739cthq0-a",
        database="sampledb_4hal",
        user="admin",
        password="HAd3geFT6UGlXXugLUgtM2226sZRXJFx",
        port=5432
    )


    return connection 

# ทดสอบเรียกใช้งาน fn 

print(connectdb())