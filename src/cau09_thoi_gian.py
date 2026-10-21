from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print("Thoi diem:", thoi_diem)
print("Kieu du lieu:", type(thoi_diem))
print("Thoi diem dang chuoi:", thoi_diem_text)
print("Kieu du lieu:", type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

thoi_luong = ket_thuc - bat_dau

print("Thoi luong:", thoi_luong)
print("Kieu du lieu:", type(thoi_luong))
