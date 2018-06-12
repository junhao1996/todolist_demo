import psycopg2
from psycopg2._psycopg import OperationalError


class TodoDB():
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", port=5432, dbname="test", user="test", password="123456")

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
        str_sql = "select * from todo where content like '%" + text + "%'"
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
        cursor = self.cursor()
        # cursor.execute("drop table if exists todo")
        # cursor.execute("create table todo(id integer primary key autoincrement ,content varchar(200))")
        cursor.execute(
            "create  todo(id SERIAL primary key,content varchar(200),status varchar(200))")

        self.conn.commit()

    def update_status(self, index, status):
        cursor = self.cursor()
        cursor.execute("update todo set status = %s where id=%s" % (status, index))

        cursor.close()
        self.conn.commit()
        self.conn.close()

    def create(self, text):
        cursor = self.cursor()
        cursor.execute("insert into todo(content,status) values ('%s','doing')" % (text,))
        cursor.close()
        self.conn.commit()
        # self.conn.close()

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
        cursor = self.cursor()
        # cursor.execute("drop table if exists todo")
        cursor.execute("alter table todo add column status varchar default 'done'")
        cursor.close()
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    todo = TodoDB()
    # todo.init__db()
    # todo.add()
    # # todo.delete()
    # todo.migrate_latest()
    # a = todo.mohu_select_content('o')
    # print(a)
    # todo.read_one()
    todo.create("sasas")
    todo.read_all()
