array = []

n = int(input('Masukkan Jumlah Kata : '))

#Menyimpan kata yang diinput dalam list
for i in range(n):
    kata = (input('Masukkan kata : '))
    array.append(kata)

print()
cari = input('Masukan kata yang ingin dicari : ')

#Mencari elemen dalam list
for i in range(n):
    if(array[i] == cari):
        print(cari, 'ditemukan pada indeks ke-', i)
        break

    if(i+1 == n):
        print('Kata tidak ditemukan')