import datetime

catatan = []

# Warna untuk tampilan
YELLOW = "\033[93m"
RESET = "\033[0m"


def tambah_catatan():
    print("\n-- Tambah Catatan Belajar --")
    mapel = input("Mapel: ").strip()
    topik = input("Topik: ").strip()

    while True:
        durasi_input = input("Durasi belajar (menit): ").strip()
        try:
            durasi = int(durasi_input)
            if durasi <= 0:
                print("Durasi harus angka positif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Masukkan angka untuk durasi (contoh: 30). Coba lagi.")

    tanggal = datetime.date.today().isoformat()

    catatan.append({
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi,
        "tanggal": tanggal,
    })

    print("Catatan berhasil ditambahkan.")


def lihat_catatan():
    print("\n-- Daftar Catatan Belajar Putri Kirana --")
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    headers = ["No", "Tanggal", "Mapel", "Topik", "Durasi (menit)"]
    rows = []
    for i, item in enumerate(catatan, start=1):
        rows.append([str(i), item['tanggal'], item['mapel'], item['topik'], str(item['durasi'])])
    cetak_tabel(headers, rows)


def total_waktu():
    total = sum(item['durasi'] for item in catatan)
    if total == 0:
        print("\nBelum ada durasi tercatat.")
        return

    jam = total // 60
    menit = total % 60
    print("\n-- Total Waktu Belajar Putri Kirana --")
    headers = ["Total (menit)", "Jam", "Menit"]
    rows = [[str(total), str(jam), str(menit)]]
    cetak_tabel(headers, rows)


def ringkasan_mingguan():
    print("\n-- Ringkasan Mingguan - Daftar Catatan Belajar Putri Kirana --")
    if not catatan:
        print("Belum ada catatan untuk dirangkum.")
        return

    hari_ini = datetime.date.today()
    mulai = hari_ini - datetime.timedelta(days=6)

    catatan_mingguan = []
    for item in catatan:
        try:
            tgl = datetime.date.fromisoformat(item['tanggal'])
        except Exception:
            continue
        if tgl >= mulai and tgl <= hari_ini:
            catatan_mingguan.append(item)

    if not catatan_mingguan:
        print("Tidak ada catatan dalam 7 hari terakhir.")
        return

    total = sum(i['durasi'] for i in catatan_mingguan)
    per_mapel = {}
    for i in catatan_mingguan:
        per_mapel.setdefault(i['mapel'], 0)
        per_mapel[i['mapel']] += i['durasi']

    print(f"Periode: {mulai.isoformat()} sampai {hari_ini.isoformat()}")
    headers = ["Mapel", "Total (menit)"]
    rows = [[m, str(d)] for m, d in sorted(per_mapel.items(), key=lambda x: x[1], reverse=True)]
    print(f"Total waktu: {total} menit")
    cetak_tabel(headers, rows)


def cetak_tabel(headers, rows):
    # Hitung lebar kolom
    cols = len(headers)
    widths = [len(h) for h in headers]
    for r in rows:
        for i, c in enumerate(r):
            widths[i] = max(widths[i], len(str(c)))

    # garis pembatas menggunakan box drawing
    top = "┌" + "┬".join("─" * (w + 2) for w in widths) + "┐"
    sep = "├" + "┼".join("─" * (w + 2) for w in widths) + "┤"
    bottom = "└" + "┴".join("─" * (w + 2) for w in widths) + "┘"

    def fmt_row(row):
        parts = []
        for i, c in enumerate(row):
            s = str(c)
            parts.append(" " + s + " " * (widths[i] - len(s) + 1))
        return "│" + "│".join(parts) + "│"

    # Warna kuning (bright yellow) untuk tampilan yang "cute"
    COLOR = "\033[93m"
    RESET = "\033[0m"

    print(COLOR + top + RESET)
    print(COLOR + fmt_row(headers) + RESET)
    print(COLOR + sep + RESET)
    for r in rows:
        print(COLOR + fmt_row(r) + RESET)
    print(COLOR + bottom + RESET)


def menu():
    print("\n" + YELLOW + "=== Study Log App ===" + RESET)
    print(YELLOW + "Putri Kirana — Cantik · Imut · Lucu · Menggemaskan" + RESET)
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Ringkasan mingguan (fitur pengembangan)")


if __name__ == "__main__":
    while True:
        menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_catatan()
        elif pilihan == "2":
            lihat_catatan()
        elif pilihan == "3":
            total_waktu()
        elif pilihan == "5":
            ringkasan_mingguan()
        elif pilihan == "4":
            print("Terima kasih, terus semangat belajar!")
            break
        else:
            print("Pilihan tidak valid")