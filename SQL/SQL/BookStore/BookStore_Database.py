import sqlite3 as sq
conn=sq.connect("DB.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE if not exists DB(id INTEGER PRIMARY KEY autoincrement,title text,author text,year INTEGER,isbn INTEGER);""")
def insertdb(b,c,d,e):    
    conn=sq.connect("DB.db")
    cursor=conn.cursor()
    DB=(b,c,d,e)
    cursor.execute("INSERT INTO DB VALUES(NULL,?,?,?,?);",DB)
    print('insert successful')
    conn.commit()
    conn.close()
def updatedb(a,b,c,d):
    conn=sq.connect("DB.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE DB SET title=?,author=?,year=?,isbn=?",(a,b,c,d))
    print('update successful')
    conn.commit()
    conn.close()
def deletedb(a):
    conn=sq.connect("DB.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM DB WHERE id=?",(a,))
    print('delete successful')
    conn.commit()
    conn.close()
def searchdb(b=None,c=None,d=None,e=None):
    conn=sq.connect("DB.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM DB WHERE title=? or author=? or year=? or isbn=?",(b,c,d,e))
    return cursor.fetchone()
    conn.commit()
    conn.close()
def viewdb():
    conn=sq.connect("DB.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM DB")
    return(cursor.fetchall())
    conn.commit()
    conn.close()