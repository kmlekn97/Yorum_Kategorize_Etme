from MySqlService import MySqlService
from DataBaseManager import DataBaseManager
from NLPManager import NLPManager
import pandas as pd
service=MySqlService()
data=DataBaseManager(service)
liste=[]
liste=data.YorumListele(service)
nlp=NLPManager()
liste_ingilizce=[]
liste_ingilizce=nlp.translatelist(liste)
result=nlp.calculatesentiment(liste_ingilizce,liste)
motion=nlp.printmotion(result)
data.AllYorumlariAnalizEt(motion,service)