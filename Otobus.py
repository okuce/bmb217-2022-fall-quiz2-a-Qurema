
class Otobus:
    plaka=""
    Nereden=""
    Nereye=""
    Dolukoltuk=0
    def __init__(self,plaka,Nereden,Nereye,Dolukoltuk):
        self.plaka= plaka
        self.Nereden= Nereden
        self.Nereye= Nereye 
        self.Dolukoltuk= Dolukoltuk
        
        
    def bilet_sat(self,satis):
        koltuk=0
        koltuk=self.Dolukoltuk
        return koltuk
        
    
    def bilet_iade(self,iade):
        boskoltuk=0
        boskoltuk= self.Dolukoltuk-iade
        return boskoltuk
        
        
        
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""

    
    def durum_yaz(self):
        print("Nereden:{}, Nereye:{}, Plaka:{}, Dolukoltuk:{}, Boskoltuk:{}".format(self.Nereden, self.Nereye, self.plaka, koltuk, boskoltuk) )
        
        """
        Alperen Öz
        """

