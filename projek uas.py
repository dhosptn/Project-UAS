import sys
total = []

print("-----------------------------------")
print("             KASIR ARDHO")
print("-----------------------------------")

def daftar_barang():
    print("| No |  Makanan/Minuman   | Harga |")
    print("-----------------------------------")
    print("| 1  | Gorengan Tahu      | 1000  |")
    print("| 2  | Risol              | 2000  |")
    print("| 3  | Bakwan             | 1000  |")
    print("| 4  | Gorengan Tempe     | 1000  |")
    print("| 5  | Es Good Day Freeze | 5000  |")
    print("-----------------------------------")
    kode = int(input("Masukkan angka makanan  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah makanan : "))
        total1 = 1000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah makanan : "))
        total2 = 2000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah makanan : "))
        total3 = 1000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah makanan : "))
        total4 = 1000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Masukkan jumlah makanan : "))
        total5 = 5000 * jumlah5   
        total.append(total5)
        tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah menu lainnya? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8/100
        elif a > 300000:
            diskon = a * 5/100
        elif a > 200000:
            diskon = a * 3/100
        elif a > 100000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print("Kembalian        : ", kembalian)
        print("-------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------")
daftar_barang()
print("Terima kasih sudah belanja ")

