ma_may = input("Nhap ma may: ")
cong_suat_w = input("Nhap cong suat W: ")
so_phut = input("Nhap so phut: ")
don_gia_kwh = input("Nhap don gia dien: ")

print("Kieu ma may:", type(ma_may))
print("Kieu cong suat ban dau:", type(cong_suat_w))
print("Kieu so phut ban dau:", type(so_phut))
print("Kieu don gia ban dau:", type(don_gia_kwh))

cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Ma may:", ma_may)
print("Cong suat:", cong_suat_w)
print("So phut:", so_phut)
print("Don gia:", don_gia_kwh)
print("Dien nang:", dien_nang_kwh, "kWh")
print("Chi phi:", chi_phi, "VND")
