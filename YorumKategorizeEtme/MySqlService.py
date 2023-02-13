from Interface.interface import implements
import pymysql.cursors
from IDataBaseService import IDataBaseService
from DBconfig import DBconfig
class MySqlService(implements(IDataBaseService),DBconfig):
    __conn=None
    __db = None
    def __init__(self):
        super().__init__()

    def connect(self):
        __db=pymysql.connect(host=self.gethost(),user=self.getuser(),password=self.getpassword(),db=self.getdb(),autocommit=True)
        self.__conn=__db.cursor()
    def Fullread(self,table,where=None):
        self.__conn.execute("Select * From {}".format(table))
        __result=self.__conn.fetchall()
        return __result
    def databasexecute(self,sql,data):
        self.__conn.execute(sql,data)
    def connectclose(self):
        self.__conn.close()