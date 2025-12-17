import csv
import heapq

# =======================
# STRUKTUR DATA PASIEN
# =======================
class Pasien:
    def __init__(self, id, nama, prioritas):
        self.id = id
        self.nama = nama
        self.prioritas = prioritas

    def __lt__(self, other):
        # priority besar dilayani lebih dulu
        return self.prioritas > other.prioritas

    def __repr__(self):
        return f"ID:{self.id}, Nama:{self.nama}, Prioritas:{self.prioritas}"


# =======================
# BACA CSV
# =======================
def baca_csv(nama_file):
    heap = []
    with open(nama_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            heapq.heappush(
                heap,
                Pasien(int(row["id"]), row["nama"], int(row["prioritas"]))
            )
    return heap


# =======================
# SIMPAN KE CSV
# =======================
def simpan_csv(nama_file, heap):
    with open(nama_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nama", "prioritas"])
        for p in heap:
            writer.writerow([p.id, p.nama, p.prioritas])


# =======================
# FITUR-FITUR
# =======================
def tampilkan_semua(heap):
    print(f"\nTotal pasien: {len(heap)}")
    for p in heap:
        print(p)


def layani_pasien(heap):
    if heap:
        p = heapq.heappop(heap)
        print("Melayani:", p)
    else:
        print("Heap kosong")


def cari_pasien(heap, id_pasien):
    for p in heap:
        if p.id == id_pasien:
            print("Ditemukan:", p)
            return
    print("Pasien tidak ditemukan")


def ubah_prioritas(heap, id_pasien, prioritas_baru):
    for p in heap:
        if p.id == id_pasien:
            p.prioritas = prioritas_baru
            heapq.heapify(heap)
            print("Prioritas berhasil diubah")
            return
    print("Pasien tidak ditemukan")


def tampilkan_teratas(heap, n):
    temp = heap.copy()
    print(f"\n{n} Pasien Prioritas Tertinggi:")
    for _ in range(min(n, len(temp))):
        print(heapq.heappop(temp))


# =======================
# MENU UTAMA
# =======================
def menu():
    print("""
===== MENU HEAP PASIEN =====
1. Tampilkan semua pasien
2. Layani pasien (pop heap)
3. Cari pasien berdasarkan ID
4. Ubah prioritas pasien
5. Tampilkan N prioritas tertinggi
6. Simpan data ke CSV
0. Keluar
""")


# =======================
# PROGRAM UTAMA
# =======================
if __name__ == "__main__":
    nama_file = "dataset_pasien_heap_500.csv"
    heap_pasien = baca_csv(nama_file)

    while True:
        menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_semua(heap_pasien)

        elif pilihan == "2":
            layani_pasien(heap_pasien)

        elif pilihan == "3":
            idp = int(input("Masukkan ID pasien: "))
            cari_pasien(heap_pasien, idp)

        elif pilihan == "4":
            idp = int(input("Masukkan ID pasien: "))
            pr = int(input("Masukkan prioritas baru: "))
            ubah_prioritas(heap_pasien, idp, pr)

        elif pilihan == "5":
            n = int(input("Berapa data teratas: "))
            tampilkan_teratas(heap_pasien, n)

        elif pilihan == "6":
            simpan_csv(nama_file, heap_pasien)
            print("Data berhasil disimpan")

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")
