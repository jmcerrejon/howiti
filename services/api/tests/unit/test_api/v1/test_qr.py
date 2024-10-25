import unittest

from pydantic import ValidationError

from schemas import QR


class TestQR(unittest.TestCase):
    def test_qr_valid_data(self):
        qr = QR(id="1", email="john.doe@example.com", qr_info={"name": "john doe"})
        self.assertEqual(qr.id, "1")
        self.assertEqual(qr.email, "john.doe@example.com")
        self.assertEqual(qr.qr_info, {"name": "john doe"})

    def test_qr_invalid_email(self):
        with self.assertRaises(ValidationError):
            QR(email="invalid-email")

    def test_qr_missing_email(self):
        with self.assertRaises(ValidationError):
            QR(email="john.doe@example.com")

    def test_qr_missing_email(self):
        with self.assertRaises(ValidationError):
            QR(name="John Doe")


if __name__ == "__main__":
    unittest.main()
