#PEP on Python
'''yaitu '''

# Sekunsial
print("Standard Code Python setelah baris kode terakhir ada new line kosong")
print("Coba bikin code print")
print('Test Pake single quote')
print('Test Pake kombinasi quote, "Apakah bisa"')

# Percabangan IF
milk_count = 0
egg_count = 0
if milk_count > 0:
    print("Membeli susu")
    if egg_count != 0:
        print("Ambil 6 Botol Susu")
    else:
        print("Ambil 1 Botol susu")
else:
    print("Tidak jadi beli susu")

# Perulangan FOR
book_count = 10
print("jumlah buku yang harus dibaca :",book_count)
read_count = 0
for read_count in range(1,book_count+1):
    print(f"Baca Buku ke-{read_count} sudah dibaca")
print("jumlah buku selesai dibaca :",read_count)

# Perulangan While
book_count = 10
print("jumlah buku :",book_count)
read_count = 0
print("jumlah buku selesai dibaca :",read_count)

while read_count < book_count:
    read_count = read_count + 1
    print(f"Baca buku yang sudah dibaca : {read_count}")
