class Kucing:
    # atribut class
    nama = ''
    warna = ''
    umur = 0

    # construktor
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    # method untuk menampilkan datanya
    def data_kucing(self):
        print(f'Nama Kucing:{self.nama}')
        print(f'Warna Kucing:{self.warna}')
        print(f'Umur Kucing:{self.umur}')