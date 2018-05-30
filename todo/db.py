import sqlite3


class TodoDB():
    def read_all(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("select * from todo")
        res = cursor.fetchall()
        result = [(i[0],i[1]) for i in res]
        return result
    def init__db(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        # cursor.execute("create table todo(id integer primary key autoincrement ,content varchar(200))")

        conn.commit()
    def add(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("insert into todo(content) values ('ewe')")
        cursor.close()
        conn.commit()
        conn.close()
if __name__ =="__main__":
    todo = TodoDB()
    # todo.init__db()
    todo.add()
    a= todo.read_all()
    print(a)