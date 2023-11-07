
from main import AES

class AES_TEST():
    def __init__(self, master_key):
        self.AES = AES(master_key)

    def test_encryption(self, plaintext):
        encrypted = self.AES.encrypt(plaintext)
        return encrypted

    def test_decryption(self, ciphertext):
        decrypted = self.AES.decrypt(ciphertext)
        return decrypted

if __name__ == '__main__':
    master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
    plaintext =  0x3243f6a8885a308d313198a2e0370734
    ciphertext = 0x3925841d02dc09fbdc118597196a0b32


    aes_test = AES_TEST(master_key)

    
    encrypted_result = aes_test.test_encryption(plaintext)
    print(f"Encrypted result: {encrypted_result:#x}")

    decrypted_result = aes_test.test_decryption(ciphertext)
    print(f"Decrypted result: {decrypted_result:#x}")