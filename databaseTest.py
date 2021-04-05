import mysql.connector as mysql

db = mysql.connect (

host = "localhost",

user = "root",

passwd = "welcometothejungle",

database = "doorActivity"

)

cursor = db.cursor()

cursor.execute("CREATE TABLE activity2( act_id INT);")