import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,jsbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title,author,year,jsbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()    
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,jsbn))
    #  to overcome the sql injection we use ? marks
    conn.commit()
    conn.close()


def search(title="",author="",year="",jsbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR jsbn=?",(title,author,year,jsbn))
    rows = cur.fetchall()
    conn.close()
    return rows    

def delete(r):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()    
    cur.execute("DELETE FROM book WHERE id=?",(r,))
    # cur.execute("ALTER TABLE book VALUES(NULL)")

    # cur.execute("ALTER TABLE book id INTEGER PRIMARY KEY")
    conn.commit()
    conn.close()


def update(id,title,author,year,jsbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()    
    cur.execute("UPDATE book SET title=?,author=?,year=?,jsbn=? WHERE id=?",(title,author,year,jsbn,id))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


connect()


# insert("hello","hello",2017,1234)
# insert("hiiii","hii",2017,1234)
# insert("cricket","aravind",2013,12345)
delete(2)
# update(3,"college","ramesh",2001,4)
print(view())
# print(search(author="siddu"))