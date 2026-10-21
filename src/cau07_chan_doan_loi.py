ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")

# Loi 1: cong_suat_w can duoc chuyen sang float de tinh toan.
# Loi 2: Ten bien khi in ket qua phai trung voi dien_nang_kwh.
