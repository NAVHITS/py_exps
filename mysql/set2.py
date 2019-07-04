import mysql.connector
db = mysql.connector.connect(host="localhost", port="3306",user="root",passwd="",database="test_db")
query = db.cursor()
data = "INSERT INTO test_tbl (name, dept) VALUES ("Naveen", "IT")"
query.execute(data)
db.commit()
print(query.rowcount, "record inserted.")
