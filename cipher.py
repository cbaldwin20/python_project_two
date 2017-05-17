class Cipher:
    """Makes a class require an encrypt and decrypt method"""
    def encrypt(self):
        """forces a class to have an ecrypt method"""
        raise NotImplementedError()

    def decrypt(self):
        """forces a class to have a decrypt method"""
        raise NotImplementedError()
    