import pandas as pd

print("💰 Perencana Keuangan Harian (Logika Rokok & Bensin mingguan)")

# Input interaktif
saldo_awal = int(input("💰 Saldo awal (Rp): "))
target_tabungan = int(input("🎯 Target tabungan (Rp): "))
jumlah_hari = int(input("🗓️ Berapa hari ingin direncanakan?: "))
makan_pagi = int(input("🍽️ Estimasi makan pagi (Rp): "))
makan_siang = int(input("🍛 Estimasi makan siang (Rp): "))
makan_malam = int(input("🍜 Estimasi makan malam (Rp): "))
bensin_perminggu = int(input("⛽ Uang bensin (permiggu) (Rp): "))
harga_rokok = int(input("🚬 Harga sebungkus rokok (Rp): "))
jumlah_rokok_perminggu = int(input("🚬 Jumlah bungkus rokok per minggu (cth: 1): "))

# Hitung
batas_pengeluaran_total = saldo_awal - target_tabungan
batas_pengeluaran_harian = batas_pengeluaran_total / jumlah_hari
total_makan = makan_pagi + makan_siang + makan_malam
rokok_perhari = (harga_rokok * jumlah_rokok_perminggu) / 7

saldo = saldo_awal
data = []

for hari in range(1, jumlah_hari + 1):
    bensin = bensin_perminggu if hari % 7 == 1 else 0
    total_harian = total_makan + bensin + rokok_perhari
    saldo -= total_harian
    data.append({
        "Hari ke": hari,
        "Makan Pagi": makan_pagi,
        "Makan Siang": makan_siang,
        "Makan Malam": makan_malam,
        "Bensin": bensin,
        "Rokok": round(rokok_perhari),
        "Total": round(total_harian),
        "Sisa Saldo": round(saldo)
    })

# Simpan ke Excel
df = pd.DataFrame(data)
df.to_excel("perencanaan_keuangan_fix.xlsx", index=False)

# Ringkasan
print(f"\n📦 Rokok dibagi rata harian: Rp {round(rokok_perhari)}")
print(f"🧾 Total pengeluaran 24 hari: Rp {round(saldo_awal - saldo)}")
print(f"💵 Sisa saldo setelah {jumlah_hari} hari & tabungan: Rp {round(saldo)}")
print("📁 Hasil disimpan di file: perencanaan_keuangan_fix.xlsx")
