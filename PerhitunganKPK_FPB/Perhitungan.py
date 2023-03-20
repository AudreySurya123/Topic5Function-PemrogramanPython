#Fungsi untuk mencari FPB
def FPB(a,b):
    if a<b:
        smaller=a
    else:
        smaller=b
    for i in range (1,smaller+1):
        if a%i==0 and b%i==0:
            FPB=i
    return FPB

#Fungsi untuk mencari KPK
def KPK(a,b):
    KPK=int(a*b/FPB(a,b))
    return KPK

#Fungsi untuk memilih menu
def show_menu():
    print("==== Program Perhitungan ====")
    print("1. KPK")
    print("2. FPB")
    print("3. Exit")
    menu = input("Pilih menu : ")

    if menu == "1": #Pilihan untuk menghitung KPK
        a = int(input('Masukkan angka pertama : '))
        b = int(input('Masukkan angka kedua   : '))
        print('KPK dari ',a,' dan ',b,' adalah ',KPK(a,b),'\n') #Untuk mencetak hasil perhitungan KPK
    elif menu == "2": #Pilihan untuk menghitung FPB
        a = int(input('Masukkan angka pertama : '))
        b = int(input('Masukkan angka kedua   : '))
        print('FPB dari ',a,' dan ',b,' adalah ',FPB(a,b)) #Untuk mencetak hasil perhitungan FPB
    elif menu == "3": #Pilihan untuk selesai
        exit()
    else:
        print("Menu tidak tersedia!") #Pilihan menu yang tidak tersedia ketika memasukkan angka selain 1-3 

if __name__ == "__main__": #Untuk perulangan menampilkan pilihan menu
    while(True):
        show_menu()
