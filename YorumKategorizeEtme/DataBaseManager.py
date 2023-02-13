class DataBaseManager():
    __IDataBaseManager=None
    def __init__(self, IDataBaseManager):
        self.__IDataBaseManager = IDataBaseManager
    def YorumListele(self,database):
        yorumlar=[]
        idler=[]
        database.connect()
        data = database.Fullread("yorumlar")
        for i in range(len(data)):
            yorumlar.append(data[i][3])
            idler.append(data[i][0])
        database.connectclose()
        return yorumlar,idler
    def YorumAnalizEt(self,database,yorum_id,yorumtype):
        database.connect()
        sql="UPDATE yorumlar SET yorum_analys = %s WHERE yorum_id = %s"
        data=(yorumtype,yorum_id)
        database.databasexecute(sql,data)
        database.connectclose()
    def AllYorumlariAnalizEt(self,motion,database):
        for yorumlar in range(len(motion[0])):
            yorum_id = motion[0][yorumlar]
            yorumtype = motion[1][yorumlar]
            self.YorumAnalizEt(database,yorum_id,yorumtype)
