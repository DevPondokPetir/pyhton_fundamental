"""
program perulangan membaca buku dengan while undefined count
"""

jumlah_buku=10
total_jumlah_baca=0
print('Ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham")
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

    #jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    #print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")
print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}")
if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print('"Bu, Semua buku sudah dibaca dan dipahami')
else:
    print(f'"Bu,tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku')




#print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
