from cipher import Cipher 

class Keyword(Cipher):
    """The 'keyword' option of encrypting/decrypting"""
    def __init__(self):
        pass

    def encrypt(self, sentence):
        """Encrypts using the 'keyword' option"""
        sentence = list(sentence)
        encrypted_sentence = []
        x = list("abcdefghijklmnopqrstuvwxyz")
        y = list("kryptos")
        for s in x:
            if s not in y:
                y.append(s)
        z = list(zip(x, y))
        z.append((" ", " "))
        for i in sentence:
            if i.lower() not in x:
                encrypted_sentence.append(i)
                continue 
            for a in z:
                if i.lower() == a[0]:
                    if i.isupper():
                        encrypted_sentence.append(a[1].upper())
                    else:
                        encrypted_sentence.append(a[1])
        encrypted_sentence = "".join(encrypted_sentence)
        return encrypted_sentence

    def decrypt(self, sentence, pad=0):
        """decrypts using the 'keyword' option"""
        sentence = list(sentence)
        decrypted_sentence = []
        x = list("abcdefghijklmnopqrstuvwxyz")
        y = list("kryptos")
        for s in x:
            if s not in y:
                y.append(s)
        z = list(zip(x, y))
        z.append((" ", " "))
        for i in sentence:
            if i.lower() not in x:
                decrypted_sentence.append(i)
                continue 
            for a in z:
                if i.lower() == a[1]:
                    if i.isupper():
                        decrypted_sentence.append(a[0].upper())
                    else:
                        decrypted_sentence.append(a[0])
        decrypted_sentence = "".join(decrypted_sentence)
        return decrypted_sentence


class Affine(Cipher):
    """Encrypts/decrypts using the 'affine' option"""
    def __init__(self):
        pass

    def encrypt(self, sentence):
        """encrypts using the 'affine' option"""
        sentence = list(sentence)
        encrypted_sentence = []
        x = list("abcdefghijklmnopqrstuvwxyz")
        y = enumerate(x)
        z = list(y)
        z.append((" ", " "))
        for i in sentence:
            if i.lower() not in x:
                encrypted_sentence.append(i)
                continue 
            for a in z:
                if i.lower() == a[1]:
                    if i.isupper():
                        new_num = (5 *(a[0]) + 8) % 26
                        for q in z:
                            if new_num == q[0]:
                                encrypted_sentence.append(q[1].upper())
                    else:
                        new_num = (5 *(a[0]) + 8) % 26
                        for q in z:
                            if new_num == q[0]:
                                encrypted_sentence.append(q[1])
        encrypted_sentence = "".join(encrypted_sentence)
        return encrypted_sentence

    def decrypt(self, sentence, pad=0):
        """decrypts using the 'affine' option"""
        sentence = list(sentence)
        decrypted_sentence = []
        x = list("abcdefghijklmnopqrstuvwxyz")
        y = enumerate(x)
        z = list(y)
        z.append((" ", " "))
        for i in sentence:

            if i.lower() not in x:
                decrypted_sentence.append(i)
                continue 
            for a in z:
                if i.lower() == a[1]:
                    if i.isupper():
                        new_num = 21 *(a[0] - 8) % 26
                        for q in z:
                            if new_num == q[0]:
                                decrypted_sentence.append(q[1].upper())
                    else:
                        new_num = 21 *(a[0] - 8) % 26
                        for q in z:
                            if new_num == q[0]:
                                decrypted_sentence.append(q[1])
        decrypted_sentence = "".join(decrypted_sentence)
        return decrypted_sentence


class Atbash(Cipher):
    """Class that encrypts/decrypts using the 'atbash' option"""
    def __init__(self):
        pass

    def encrypt(self, sentence):
        """encrypts using the 'atbash' option"""
        sentence = list(sentence)
        encrypted_sentence = []
        x = list("abcdefghijklmnopqrstuvwxyz")
        y = x[::-1]
        z = list(zip(x, y))
        z.append((" ", " "))
        for i in sentence:
            if i.lower() not in x:
                encrypted_sentence.append(i)
                continue 
            for a in z:
                if i.lower() == a[0]:
                    if i.isupper():
                        encrypted_sentence.append(a[1].upper())
                    else:
                        encrypted_sentence.append(a[1])
        encrypted_sentence = "".join(encrypted_sentence)
        return encrypted_sentence

    def decrypt(self, sentence, pad=0):
        """decrypts using the 'atbash' option """
        sentence = list(sentence)
        decrypted_sentence = []
        x = list("abcdefghijklmnopqrstuvwxyz")
        y = x[::-1]
        z = list(zip(x, y))
        z.append((" ", " "))
        for i in sentence:
            if i.lower() not in x:
                decrypted_sentence.append(i)
                continue 
            for a in z:
                if i.lower() == a[1]:
                    if i.isupper():
                        decrypted_sentence.append(a[0].upper())
                    else:
                        decrypted_sentence.append(a[0])
        decrypted_sentence = "".join(decrypted_sentence)
        return decrypted_sentence