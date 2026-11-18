class ManajerInventori:
    def __init__(self):
        # Dictionary: nama barang -> jumlah stok
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah <= 0:
            return "Jumlah tambah harus positif"
        if nama in self.inventori:
            self.inventori[nama] += jumlah
        else:
            self.inventori[nama] = jumlah
        return f"Berhasil tambah {jumlah} {nama}. Stok {nama}: {self.inventori[nama]}"

    def hapus_barang(self, nama, jumlah):
        if nama not in self.inventori:
            return f"Barang {nama} tidak ada di inventori"
        if not 0 < jumlah <= self.inventori[nama]:
            return f"Stok {nama} tidak mencukupi"
        self.inventori[nama] -= jumlah
        sisa = self.inventori[nama]
        if sisa == 0:
            del self.inventori[nama]
            return f"Berhasil kurangi {jumlah} {nama}. Stok habis, barang dihapus dari inventori"
        return f"Berhasil kurangi {jumlah} {nama}. Stok {nama}: {sisa}"

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"
        daftar = ["Daftar Inventori:"]
        for no, (nama, jumlah) in enumerate(self.inventori.items(), start=1):
            daftar.append(f"{no}. {nama}: {jumlah}")
        return "\n".join(daftar)


# Demonstrasi semua method
gudang = ManajerInventori()

print(gudang.lihat_inventori())
print(gudang.tambah_barang("Buku", 50))
print(gudang.tambah_barang("Pensil", 100))
print(gudang.tambah_barang("Buku", 20))       # menambah stok barang yang sudah ada
print(gudang.lihat_inventori())

print(gudang.hapus_barang("Buku", 30))        # mengurangi stok
print(gudang.hapus_barang("Pensil", 150))     # stok tidak mencukupi
print(gudang.hapus_barang("Penghapus", 5))    # barang tidak ada
print(gudang.hapus_barang("Pensil", 100))     # stok habis -> barang dihapus
print(gudang.lihat_inventori())