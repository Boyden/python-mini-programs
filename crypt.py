from Crypto.Cipher import AES

class AESCrypto():
	
	def __init__(self, IV = None, mode = AES.MODE_CFB):
		self.IV = IV
		self.mode = mode

	def encrypt(self, str, key):
        while len(key)%16 != 0:
        	key += " "
		cipher = AES.new(key.encode("utf-8"), self.mode, IV)
		return cipher.encrypt(str.encode("utf-8")).hex()

    def decrypt(self, str, key):
    	while len(key)%16 != 0:
        	key += " "
    	cipher = AES.new(key.encode("utf-8"), AES.MODE_CFB, IV)
    	return cipher.decrypt(bytes.fromhex(str)).decode("utf-8")

IV = "9876543210000000000000"[0:AES.block_size].encode("utf-8")
key = "hello"
s = "a stu den"
cipher = AESCrypto(IV)
s = cipher.encrypt(s, key)
print(f"encrypt string:{s}")
s = cipher.decrypt(s, key)
print(f"decrypt string:{s}")