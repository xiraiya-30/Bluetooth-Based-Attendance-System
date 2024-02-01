import sqlite3, blth
import datetime,time

db = sqlite3.connect('attendance.db')
cursor=db.cursor()

d_t = str(datetime.datetime.now()).split(".")[0]
#cursor.execute('DROP TABLE ATDN')
try:
    cursor.execute("SELECT '{}' from ATDN".format(d_t))
except:
    cursor.execute('''CREATE TABLE ATDN(
               Bt_Address VARCHAR(50))''')

    cursor.execute('''INSERT INTO ATDN(Bt_Address)
        VALUES ('24:29:34:7E:CE:EA'),('34:47:9A:B2:66:EA'),
        ('58:D6:97:14:8A:08')''')
    x='34:47:9A:B2:66:'
    for i in range(1,60):
        cursor.execute('''INSERT INTO ATDN(Bt_Address)
                          VALUES (?)''',(x+str(i),))


cursor.execute('''ALTER TABLE ATDN ADD COLUMN '{}' INTEGER'''.format(d_t))
cursor.execute("UPDATE ATDN SET '{}' = 0".format(d_t))

available_devices = blth.scan()

for i in available_devices:
    cursor.execute('''UPDATE ATDN 
                      SET '{}' = 1
                      WHERE Bt_Address = '{}' '''.format(d_t, i))






table = cursor.execute('SELECT * from ATDN')
header=[]
for i in table.description:
    header.append(i[0])
items=[]
for row in table:
    items.append(list(row))


from tabulate import tabulate
print("\nAttendance marked!!!\n")
print(tabulate(items,header))


db.commit()
db.close()





