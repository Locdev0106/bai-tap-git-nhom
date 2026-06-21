import unittest
from main import tinh_diem_gpa

class TestGPA(unittest.TestCase):
    def test_gpa_tuyen_tinh(self):
        # Kiểm tra điểm tuyến tính (dưới 8.5)
        # Điểm hệ 10 là 7.0 thì GPA hệ 4 phải là 2.8
        self.assertEqual(tinh_diem_gpa(7.0), 2.8)

    def test_gpa_can_tren(self):
        # Kiểm tra điểm xuất sắc (>= 8.5)
        # Điểm hệ 10 là 8.5 thì GPA hệ 4 phải là 4.0
        self.assertEqual(tinh_diem_gpa(8.5), 4.0)

if __name__ == '__main__':
    unittest.main()