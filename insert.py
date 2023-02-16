import sqlite3
conn=sqlite3.connect('mark5.db')
print("Open database Successfully")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1,'MARK',30,'MANGU','MALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (2,'MASEK',50,'ALLIANCE','MALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (3,'MARCUS',40,'ALLIANCE','MALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (4,'TIMO',20,'ALLIANCE','FEMALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (5,'JJ',70,'MOI FORCES','MALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (6,'SYLVIA',100,'MOI GIRLS','FEMALE')")

conn.commit()
print("Records added successfully")
conn.close()