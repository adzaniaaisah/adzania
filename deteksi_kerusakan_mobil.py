"""
Program Pendeteksi Sistem Kerusakan Mobil

Deskripsi:
Program ini membantu mendeteksi kemungkinan kerusakan pada sistem mobil berdasarkan gejala yang dimasukkan oleh pengguna.
"""

# Daftar gejala dan kemungkinan kerusakan
GEJALA_KERUSAKAN = {
    "mobil sulit dinyalakan": "Masalah pada aki atau sistem starter",
    "lampu redup": "Aki lemah atau alternator bermasalah",
    "mesin overheating": "Radiator bocor atau kipas pendingin rusak",
    "asap knalpot berwarna putih": "Kebocoran pada gasket kepala silinder",
    "rem berbunyi": "Kampas rem aus atau cakram bermasalah",
    "getaran saat kecepatan tinggi": "Ban tidak seimbang atau suspensi rusak",
    "oli bocor": "Seal mesin atau gasket rusak",
    "mesin mati mendadak": "Masalah pada sistem bahan bakar atau pengapian",
    "transmisi tidak responsif": "Oli transmisi kurang atau komponen transmisi rusak",
    "setir berat": "Pompa power steering bermasalah atau oli power steering kurang"
}

def tampilkan_gejala():
    print("\nDaftar Gejala:")
    for idx, gejala in enumerate(GEJALA_KERUSAKAN.keys(), 1):
        print(f"{idx}. {gejala}")

def deteksi_kerusakan(pilihan):
    gejala_list = list(GEJALA_KERUSAKAN.keys())
    if 1 <= pilihan <= len(gejala_list):
        gejala = gejala_list[pilihan - 1]
        kerusakan = GEJALA_KERUSAKAN[gejala]
        print(f"\nGejala: {gejala}\nKemungkinan Kerusakan: {kerusakan}")
    else:
        print("Pilihan tidak valid.")

def main():
    print("=== Sistem Pendeteksi Kerusakan Mobil ===")
    tampilkan_gejala()
    try:
        pilihan = int(input("\nMasukkan nomor gejala yang dialami: "))
        deteksi_kerusakan(pilihan)
    except ValueError:
        print("Input harus berupa angka.")

if __name__ == "__main__":
    main()
