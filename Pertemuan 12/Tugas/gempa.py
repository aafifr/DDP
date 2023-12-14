class gempa:
    # atribut class
    lokasi = ''
    skala = 0

    # construktor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # method untuk menampilkan data
    def dampak(self):
        if self.skala < 2:
            ket = ('Dampak Gempa Tidak Berasa')
        elif self.skala > 2:
            ket = ('Dampak Gempa: Bangunan retak-retak')
        elif self.skala > 4:
            ket = ('Dampak Gempa: Bangunan Roboh')
        elif self.skala > 6:
            ket = ('Dampak Gempa:Bangunan Roboh & Berpotensi Tsunami')
        else:
            ket = ('Dampak Gempa Tidak ditemukan')
        
        print(f'Lokasi:{self.lokasi}')
        print(f'Skala:{self.skala}')
        print(f'Keterangan:{ket}')