cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Cong suat:", cong_suat_w, type(cong_suat_w))
print("So phut:", so_phut, type(so_phut))
print("Don gia:", don_gia_kwh, type(don_gia_kwh))
print("Dien nang:", dien_nang_kwh, "kWh")
print("Chi phi:", chi_phi, "VND")
print("Kieu du lieu dien nang:", type(dien_nang_kwh))
print("Kieu du lieu chi phi:", type(chi_phi))
