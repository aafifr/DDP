from gempa import *

banten = gempa('Banten', 1.2)
palu = gempa('Palu', 6.1)
cianjur = gempa('Cianjur', 5.6)
jayapura = gempa('Jayapura', 3.3)
garut = gempa('Garut', 4.0)

banten.dampak()
palu.dampak()
cianjur.dampak()
jayapura.dampak()
garut.dampak()