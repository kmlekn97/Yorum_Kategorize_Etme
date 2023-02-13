from textblob import TextBlob
from googletrans import Translator
class NLPManager():
    def translatelist(self,liste):
        translator = Translator()
        liste_ingilizce = []
        for yazi in liste[0]:
            blob = TextBlob(yazi)
            blob_gelen = str(blob)
            blob_eng = translator.translate(blob_gelen)
            liste_ingilizce.append(str(blob_eng.text))
        return liste_ingilizce
    def calculatesentiment(self,liste_ingilizce,liste):
        polarity=[]
        id=[]
        for yazi in range(len(liste_ingilizce)):
            blob = TextBlob(liste_ingilizce[yazi])
            polarity.append(blob.polarity)
            id.append(liste[1][yazi])
        return polarity,id
    def findemotion(self,polarity):
        if polarity>0.0:
            return "olumlu"
        elif polarity<0.0:
            return "olumsuz"
        elif polarity==0.0:
            return "nötr"
        else:
            return "İşleniyor"
    def  printmotion(self,result):
        i=0
        id=[]
        duygu=[]
        for motion in result[0]:
            duygu.append(self.findemotion(motion))
            id.append(result[1][i])
            i+=1
        return id,duygu

