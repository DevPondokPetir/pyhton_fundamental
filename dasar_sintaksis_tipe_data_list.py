
daftar_buku=['The lord of the rings', 'Harry Potter', 'The Secret',100]
print('Tampilkan variable didalam daftar_buku')
print(daftar_buku)

print('\nProcess tampilkan semua dengan for in')
for buku in daftar_buku:
    print(buku)
print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[1])
print(daftar_buku[2])

print('\nTampilkan daftar_buku dengan for in range')
for i in range(0, len(daftar_buku)):
    print (daftar_buku[i])

print('Tambahkan satu buku baru ')
daftar_buku.append('Seven Habits')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClearList')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMengganti elemen pertama')
daftar_buku=['The lord of the rings', 'Harry Potter', 'The Secret', 100]
daftar_buku[0] = 'The king of the rings'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke - 2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku=['The lord of the rings', 'Harry Potter', 'The Secret', 100]
#pop tanpa variable indexs akan mengambil nilai yang paling akhir
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nPop -1')
daftar_buku=['The lord of the rings', 'Harry Potter', 'The Secret', 100]
#pop denga variabel indexs akan mengambil nilai ke-n dari nilai yang paling akhir
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku=['The lord of the rings', 'Harry Potter', 'The Secret', 100]
print('\nPerintah Del')
#del dengan variable indexs
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])



daftar_buku=['The lord of the rings', 'Harry Potter', 'The Secret', 100]
print('\nPerintah Del dengan list comprehension')
#del dengan variable indexs
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku=['The lord of the rings', 'Harry Potter', 'The Secret', 100]
print('\nPerintah Del dengan list comprehension 1')
#del dengan variable indexs
del daftar_buku[0:2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku=['The lord of the rings', 'Harry Potter', 'The Secret', 100]
print('\nPerintah Del dengan list comprehension 2')
#del dengan variable indexs
del daftar_buku[0:-4]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku=['The lord of the rings', 'Harry Potter', 'The Secret', 100]
print('\nPerintah Del dengan list comprehension 3')
#del dengan variable indexs
del daftar_buku[0::2] #start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


