import sqlite3


class TodoDB():
    def read_all(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("select * from todo order by id desc")
        res = cursor.fetchall()
        # result = [(i[0],i[1]) for i in res]
        return res
    def read_one(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("select * from todo order by id desc limit 0,1")
        res = cursor.fetchall()
        return res
    def read_kongque(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("select * from todo order by id desc limit 0,1")
        res = cursor.fetchall()
        return res
    def init__db(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        # cursor.execute("drop table if exists todo")
        cursor.execute("create table todo(id integer primary key autoincrement ,content varchar(200))")

        conn.commit()
    def add(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("insert into todo(content) values ('ewe')")
        cursor.close()
        conn.commit()
        conn.close()
    def delete(self,index):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todo WHERE id = %d;"%(index))
        cursor.close()
        conn.commit()
        conn.close()
if __name__ =="__main__":
    todo = TodoDB()
    # todo.init__db()
    todo.add()
    # todo.delete()
    a= todo.read_all()
    b = todo.read_one()
    print(b)
    print(a)