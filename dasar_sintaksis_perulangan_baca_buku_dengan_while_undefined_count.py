"""
program perulangan membaca buku dengan while undefined count
"""

book_count=10
read_count=0
print('Ibu berkata, "baca semua bukumu"')

understood_count= 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {understood_count}')

while read_count < book_count:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Buku ke {understood_count + 1} belum paham")
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah dibaca dan dipahami")

    #jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    #print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")
print(f"Jumlah buku yang sudah dibaca dan dipahami {understood_count}")
if understood_count == book_count:
    print('"Bu, Semua buku sudah dibaca dan dipahami')
else:
    print(f'"Bu,tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {understood_count} buku')




#print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
