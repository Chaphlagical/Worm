import sqlite3
from get_data import*

class DB():
    def __init__(self):
        self.conn=None
        self.cursor=None
        self.selection=None
        
    def init(self):
        self.conn=sqlite3.connect('./data/data.db')
        print ("Opened database successfully")
        self.cursor=self.conn.cursor()
        self.cursor.execute('''CREATE TABLE INFO
                           (YEAR                INT      NULL,
                            年末总人口           FLOAT    NULL,
                            男性人口             INT      NULL,
                            女性人口             INT      NULL,
                            城镇人口             INT      NULL,
                            乡村人口             INT      NULL,
                            低龄人口             INT      NULL,
                            中龄人口             INT      NULL,
                            老龄人口             INT      NULL,
                            研究生招生数          INT      NULL,
                            研究生在学人数        INT      NULL,
                            研究生毕业人数        INT      NULL,
                            出国留学人员          INT      NULL,
                            学成回国留学人员       INT      NULL,
                            用水总量             FLOAT     NULL,
                            农业用水总量          FLOAT     NULL,
                            工业用水总量          FLOAT     NULL,
                            生活用水总量          FLOAT     NULL,
                            生态用水总量          FLOAT     NULL,
                            人均用水量           FLOAT      NULL);''')
        print("Table created successfully")
        for year in range(1999,2019):
            self.conn.execute("INSERT INTO INFO (YEAR) VALUES ("+str(year)+")")

        print("Table init successfully")
    
    def update(self,name,dict):
        for year in dict.keys():
            
            self.cursor.execute("UPDATE INFO set "+name.upper()+" = "+str(dict[year])+" where YEAR="+str(year))
        self.conn.commit()
        print("Total number of rows updated :", self.conn.total_changes)
    
    def select(self,name):
        self.selection={}
        cursor = self.cursor.execute("SELECT YEAR, "+name.upper()+"  from INFO")
        for row in cursor:
            self.selection[row[0]]=row[1]

    
    def save(self):
        self.conn.commit()
        self.conn.close()

    


