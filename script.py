import psycopg2

DB_HOST='localhost'
DB_NAME='postgres'
DB_USER='postgres'
DB_PASS='root'


conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
cur=conn.cursor()

#Create a table
cur.execute("create table student(id SERIAL PRIMARY KEY,name VARCHAR)")

#Inserting into a table
cur.execute("insert into student (name) values(%s)", ("Nehal",))

#Reading a table
cur.execute("select * from student")
print(cur.fetchall())

cur.execute('Select * from student where id=%s',(1,))
print(cur.fetchone())

# Updating a field in db
cur.execute("UPDATE student SET age = 25 WHERE id = 2")

# Displaying one row of table
cur.execute('select * from messages')
print(cur.fetchone())

# Adding a new column path to existing table (Change table name)
cur.execute('ALTER TABLE messages ADD path varchar(50)')
cur.execute('select * from messages')
print(cur.fetchone())

conn.commit()
#print(cur.execute('select * from public.messages;'))

cur.close()
conn.close()
