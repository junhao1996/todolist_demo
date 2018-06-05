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
        return res[0]

    def mohu_select_content(self, text):
        cursor = self.cursor()
        str_sql = "select * from todo where content like '%"+text+"%'"
        cursor.execute(str_sql)
        res = cursor.fetchall()
        return res

    def read_id(self, index):
        cursor = self.cursor()
        cursor.execute("select id,content,status from todo where id = ?", (index,))
        res_data = cursor.fetchone()
        for i in res_data:
            print(i)

        print(res_data)
        return res_data

    def init__db(self):
        conn = sqlite3.connect('test.db')
        cursor = self.cursor()
        # cursor.execute("drop table if exists todo")
        # cursor.execute("create table todo(id integer primary key autoincrement ,content varchar(200))")
        cursor.execute(
            "create table IF not EXISTS todo(id integer primary key autoincrement ,content varchar(200),status varchar(200))")

        conn.commit()

    def update_status(self, index, status):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("update todo set status = ? where id=?", (status, index))

        cursor.close()
        conn.commit()
        conn.close()

    def create(self, text):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("insert into todo(content,status) values (?,'doing')", (text,))

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

    def migrate_latest(self):
        #     迁移
        self.init__db()
        self.s2_add_status_column()

    def s2_add_status_column(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        # cursor.execute("drop table if exists todo")
        cursor.execute("alter table todo add column status varchar default 'done'")
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == "__main__":
    todo = TodoDB()
    # todo.init__db()
    # todo.add()
    # # todo.delete()
    # todo.migrate_latest()
    a = todo.mohu_select_content('o')
    print(a)
    # a = 1 or 3
    # print(a)
    # b = 1 and 3
    # print(b)
    # c = 0 and 1 and 2
    # print(c)
    # d = 0 and 2 or 1
    # print(d)
    # aa = None or 0
    # print(aa)
