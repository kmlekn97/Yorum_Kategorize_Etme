from Interface.interface import Interface
class IDataBaseService(Interface):
    def connect(self):
        pass
    def Fullread(self,table,where=None):
        pass
    def databasexecute(self,sql,data):
        pass
    def connectclose(self):
        pass