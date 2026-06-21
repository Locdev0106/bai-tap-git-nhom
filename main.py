def tinh_diem_gpa(diem_so):
    if diem_so >= 8.5:
        return 4.0  # Code của Dev B
    else:
        return ((diem_so / 10) * 3.5)  # Code của Dev A
print("Điểm GPA của hệ 4 là:",tinh_diem_gpa(8.5))
