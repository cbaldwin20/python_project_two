from cipher import Cipher 
import random 

def cls():
    """adds two line spaces"""
    print("")
    print("")
    
class OneTimePad(Cipher):
    """Class that creates or uses a one time pad"""
    def __init__(self):
        pass

    def encrypt(self, sentence):
        """encrypts and outputs a one time use pad"""
        sentence = list(sentence)
        encrypted_sentence = []
        x = list("abcdefghijklmnopqrstuvwxyz")
        l = len(x)
        y = random.sample(x, l)
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
        y = "".join(y)
        cls()
        print("Your one time use pad is: {}".format(y))
        print("")
        return encrypted_sentence

    def decrypt(self, sentence, pad):
        """decrypts using a one time use pad"""
        sentence = list(sentence)
        decrypted_sentence = []
        x = list("abcdefghijklmnopqrstuvwxyz")
        l = len(x)
        y = pad 
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