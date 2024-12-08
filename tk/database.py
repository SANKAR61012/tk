import sqlite3


class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.c=self.con.cursor()
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS data(
        pid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age TEXT NOT NULL,
        gender TEXT NOT NULL,
        address TEXT NOT NULL,
        contact TEXT NOT NULL,
        mail TEXT NOT NULL
        )

        """)
        self.con.commit()

    def insert(self, name, age, gender, address, contact, mail):
        sql="""
           insert into data values(NULL,?,?,?,?,?,?)
        """
        self.c.execute(sql,(name,age,gender,address,contact,mail))
        self.con.commit()

    def fetch_record(self):
        self.c.execute("SELECT * FROM data")
        data= self.c.fetchall()
        return data

    def update_record(self,name,age,gender,address,contact,mail,pid):
        sql="""
           update data set name=?,age=?,gender=?,address=?,contact=?,mail=? where pid=?
        """
        self.c.execute(sql,(name,age,gender,address,contact,mail,pid))
        self.con.commit()

    def remove_record(self, pid):
        sql= "delete from data where pid=?"
        self.c.execute(sql, (pid,))
        self.con.commit()

