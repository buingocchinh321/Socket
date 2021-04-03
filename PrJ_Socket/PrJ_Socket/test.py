import pyodbc


server = 'LAPTOP-EAK56VKK\SQLEXPRESS'
database = 'QLyTiSoTranDau'
username = 'buingocchinh321' 
password = 'chinh016688' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

cursor.execute("select Username, Pass from ThongTinKH")
u = cursor.fetchall()
for row in u:
    print(row.Username,row.Pass)

