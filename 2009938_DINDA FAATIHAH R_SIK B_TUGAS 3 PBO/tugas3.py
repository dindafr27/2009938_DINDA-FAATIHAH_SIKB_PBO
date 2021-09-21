class segitiga:
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas_segitiga(self):
        print((self.alas*self.tinggi)/2)

class balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume_balok(self):
        print(self.panjang*self.lebar*self.tinggi)
    
segitiga = segitiga(
    alas= 15,
    tinggi= 12
)

balok = balok(
    panjang= 15,
    lebar= 5,
    tinggi= 4
)

segitiga.luas_segitiga()
balok.volume_balok()
        
        
        