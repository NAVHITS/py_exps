import mysql.connector
db = mysql.connector.connect(host="localhost", port="3306",user="root",passwd="",database="test_db")
query = db.cursor()
query.execute("CREATE TABLE test_tbl (name VARCHAR(25), dept VARCHAR(10))")
db.commit()
