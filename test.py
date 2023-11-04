import unittest
from aes import AES

class AES_TEST(unittest.TestCase):
    def setUp(self):
        master_key = 0x2b7e151628aed2a6abf7158809cf4f3c2b7e151628aed2a6abf7158809cf4f3c
        self.AES = AES(master_key)

    def test_encryption(self):
        plaintext = 0x3243f6a8885a308d313198a2e03707343243f6a8885a308d313198a2e0370734
        encrypted = self.AES.encrypt(plaintext)

        expected_encrypted = 0x3925841d02dc09fbdc118597196a0b32
        self.assertEqual(encrypted, expected_encrypted, "Помилка шифрування")

    def test_decryption(self):
        plaintext = 0x3243f6a8885a308d313198a2e0370734  # 128-бітові вхідні дані
        encrypted = self.AES.encrypt(plaintext)

        decrypted = self.AES.decrypt(encrypted)

        self.assertEqual(decrypted, plaintext, "Помилка розшифрування")

if __name__ == '__main__':
    unittest.main()