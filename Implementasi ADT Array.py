# Input ukuran array
size = int(input("Masukkan ukuran array: "))

if size <= 0:
    print("Ukuran array tidak valid!")
else:
    data = [0] * size

    def tampilkan_array(arr):
        print("\nIsi array:")
        for i in range(len(arr)):
            print(f"Index {i} = {arr[i]}")

    # Mengisi array
    for i in range(size):
        nilai = int(input(f"Masukkan nilai untuk index {i}: "))
        data[i] = nilai

    tampilkan_array(data)

    # Mengakses elemen
    idx = int(input("\nMasukkan index yang ingin diambil: "))
    if 0 <= idx < size:
        print("Nilai pada index tersebut adalah:", data[idx])
    else:
        print("Index di luar batas!")

    # Mencari nilai
    cari = int(input("\nMasukkan nilai yang ingin dicari: "))
    if cari in data:
        print("Nilai ditemukan pada index:", data.index(cari))
    else:
        print("Nilai tidak ditemukan.")
