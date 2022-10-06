class Otobus:
    plaka=""
    Nereden=""
    Nereye=""
    Boskoltuk=0
    Dolukoltuk=0
    def __init__(self,plaka,Nereden,Nereye,Boskoltuk,Dolukoltuk):
        self.plaka= plaka
        self.Nereden= Nereden
        self.Nereye= Nereye 
        self.Bsokoltuk=Boskoltuk
        self.Dolukoltuk= Dolukoltuk
        
        
    def bilet_sat(self,Dolukoltuk):
        koltuk=0
        koltuk= (self.Dolukoltuk + 1)
        return koltuk
        
    
    def bilet_iade(self,Boskoltuk):
        boskoltuk=0
        boskoltuk= (koltuk-1)
        return boskoltuk
        
        
        
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""

    
    def durum_yaz(self):
        print("Nereden:{}, Nereye:{}, Plaka:{}, Dolukoltuk:{}, Boskoltuk:{}".format(self.Nereden, self.Nereye, self.Plaka, koltuk, boskoltuk) )


