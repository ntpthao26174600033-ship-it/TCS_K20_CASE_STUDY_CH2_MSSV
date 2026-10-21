from datetime import datetime

ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut su dung: "))
don_gia_kwh = float(input("Nhap don gia dien: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n===== THONG TIN SU DUNG MAY =====")
print("Ma phien:", ma_phien)
print("Ma may:", ma_may)
print("Cong suat:", cong_suat_w, "W")
print("Thoi gian:", so_phut, "phut")
print("Dien nang:", dien_nang_kwh, "kWh")
print("Chi phi:", chi_phi, "VND")