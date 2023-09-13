daftar_buku = ["Seven Habits", "Rich Dad Poor Dad", "How to Influence People"]
print("Tampilkan List daftar buku")
print(daftar_buku)

print("\nTampilkan daftar buku dengan for")
for i in daftar_buku:
    print(i)

print("\nTampilkan daftar buku pada index tertentu")
print("Index Pertama:", daftar_buku[0])
print("Index Ketiga:", daftar_buku[-1])
print("Index Kedua:", daftar_buku[1])



print("\nTampilkan daftar buku dengan for in range")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMencoba Fitur Dinamically Type Language Python, menugaskan variabel dengan nilai lain")
daftar_buku = [1, "Number One", 1.2, "Point Four"]
print(daftar_buku)
print("\nMenambahkan nilai pada daftar_buku")
daftar_buku.append("Kisah Tanah Jawa")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMenghapus semua isi daftar buku")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMengganti elemen pertama")
daftar_buku = [1, "Number One", 1.2, "Point Four"]
daftar_buku[0] = "BUKU SATU"
print(daftar_buku)

print("\nMengambil nilai kedua pada daftar_buku")
daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
