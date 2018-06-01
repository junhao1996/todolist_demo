import sqlite3


class TodoDB():
    def __init__(self):
        self.conn = sqlite3.connect('test.db')

    def cursor(self):
        return self.conn.cursor()
    def read_all(self):
        cursor = self.cursor()
        cursor.execute("select * from todo order by id desc")
        res = cursor.fetchall()
        print(res)
        # result = [(i[0],i[1]) for i in res]
        return res

    def read_one(self):
        cursor = self.cursor()
        cursor.execute("select * from todo order by id desc limit 0,1")
        res = cursor.fetchall()
        return res[1]

    def read_id(self, index):
        cursor = self.cursor()
        cursor.execute("select id,content from todo where id = ?", (index,))
        res_data = cursor.fetchone()
        # cursor.close()
        print(res_data)
        return res_data

    def init__db(self):
        conn = sqlite3.connect('test.db')
        cursor = self.cursor()
        # cursor.execute("drop table if exists todo")
        cursor.execute("create table todo(id integer primary key autoincrement ,content varchar(200))")

        conn.commit()

    def create(self, text):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("insert into todo(content) values (?)", (text,))
        cursor.close()
        conn.commit()
        conn.close()

    def delete(self, index):
        cursor = self.cursor()
        cursor.execute("DELETE FROM todo WHERE id = %d;" % (index))
        cursor.close()
        self.conn.commit()
        self.conn.close()
        return "delete"
    def close(self):
        self.cursor().close()
        self.conn.close()

if __name__ == "__main__":
    todo = TodoDB()
    # todo.init__db()
    # todo.add()
    # # todo.delete()
    # a = todo.read_all()
    # b = todo.read_one()
    # print(b)
    # print(a)
    todo.read_id(5)
    # todo.read_all()
