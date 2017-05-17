from onetimepad import OneTimePad 
from options import Affine
from options import Atbash
from options import Keyword
from fivespaces import FiveSpaces 

def cls():
    """adds two line spaces"""
    print("")
    print("")

class Play():
    """class that that starts the program"""
    def __init__(self):
        self.pad = 0

        while True:
            #Gives option to either encrypt or decrypt
            self.action = input("Do you want to either encrypt OR " 
                             "decrypt a sentence? Enter 'e' or 'd': ")
            self.action = self.action.strip()
            if self.action.upper() in ["ENCRYPT", "E", "DECRYPT", "D"]:
                break 
            else:
                cls()
                print("'{}'' was not an option.".format(self.action)) 

        while True: 
            #Asks for sentence less than 84 character if encrypting, 
            #or gets sentence for decrypting.
            cls()
            print("What is your sentence?")
            if self.action.upper() in ["ENCRYPT", "E"]: 
                print("(Sentences cannot be longer than 83 characters."
                      " Example below: )")
                print("We are the champions, my friends. And we'll " 
                      "keep on fighting till the end. We are t")
                self.sentence = input(" :")
                self.sentence = self.sentence.strip()
                if len(self.sentence) < 84:
                    break 
                else:
                    cls()
                    print("Sorry but your sentence was longer than "
                          "84 characters.")
            else:
                self.sentence = input(" :")
                self.sentence = self.sentence.strip()
                break
        cls()
        print("Which method do you want to use?")
        print("")
        while True:
            print("Enter 'At' for the Atbash technique.")
            print("Enter 'Af' for the Affine technique.")
            print("Enter 'K' for the Keyword technique.")
            print("Enter 'P' for the one time use pad technique.")
            self.way = input(": ")
            self.way = self.way.strip()
            if self.way.upper() == 'AT':
                self.way = Atbash  
                break
            elif self.way.upper() == 'AF':
                self.way = Affine 
                break
            elif self.way.upper() == 'K':
                self.way = Keyword  
                break
            elif self.way.upper() == 'P':
                self.way = OneTimePad
                if self.action.upper() in ["DECRYPT", "D"]:
                    cls()
                    self.pad = input("Please enter the one time use"
                                    " pad: ")
                break
            else:
                cls()
                print("'{}' was not an option.".format(self.way))
        #sends the sentence off to be either encrypted or decrypted
        if self.action.upper() in ["ENCRYPT", "E"]:
            self.return_sentence = self.way().encrypt(self.sentence)
            self.return_sentence = \
                FiveSpaces().encrypt_five(self.return_sentence)
        elif self.action.upper() in ["DECRYPT", "D"]:
            self.updated_sentence = \
                FiveSpaces().decrypt_five(self.sentence)
            self.return_sentence = \
            self.way().decrypt(self.updated_sentence, self.pad)

    def __str__(self):
        return self.return_sentence