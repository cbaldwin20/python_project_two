import random

class FiveSpaces:
    """Class that evens out the sentence into blocks of five"""
    
    def encrypt_five(self, x):
        """encrypts the sentence into blocks of five"""
        for_indexes = list(enumerate("abcdefghijklmnopqrstuvwxyzABCDE"
        "FGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-`~\|]}[{';:/?.>,<"))
        y = list(enumerate(x)) 
        w = "abcdefghijklmnopqrstuvwxyz"
        z = list(enumerate(w))
        #does the list 'indexes'. Index number where the space is. 
        indexes = []
        for index, letter in y:
            if letter == " ":
                indexes.append(index) 
        #got how long the indexes was (how many spaces), and converted
        # it into a letter. 
        end_letter = len(indexes)
        for a, b in z:
            if end_letter == a:
                end_letter = b 
        #goes through the number indexes we have, and assigns them a 
        #letter and puts them in the list 'letter_indexes'
        letter_indexes = []
        for i in indexes:
            for a, b in for_indexes:
                if i == a:
                    letter_indexes.append(b) 
        #mixing up the order of the indexes so its not obvious when I 
        #append them. 
        random.shuffle(letter_indexes)
        #sticking the letter indexes all at the end of x
        x = list(x)
        x.extend(letter_indexes)
        #sticking how many indexes for spaces at the front in letter
        # form
        x.insert(0, end_letter)
        x = "".join(x)   
        x = x.replace(" ", "")
        x = list(x)
        #putting in a filler letter to be replaced when I get the 
        #remainder number letter      
        x.insert(0, "$")
        #now I'm seeing how many I need to make divisible by 5
        remainder = len(x) % 5
        remainder = 5 - remainder 
        #putting the remainder amount into letter form
        for a, b in z:
            if remainder == a:
                remainder_letter = b
        #Now removing the "$" filler from the front, and adding 
        #another letter to the front that represents how many to take
        # off the end and discard. The remainders.  
        del x[0]
        x.insert(0, remainder_letter)
        #making it so the sentence is divisible by 5
        while remainder:
            x.append(random.choice(w))
            remainder -= 1
        #now adds a space every five characters
        a = 1
        for i in x:
            if a % 6 == 0:
                x.insert(a - 1, " ")
            a += 1
        x = "".join(x)
        return x 

    def decrypt_five(self, x):
        """decrypts the sentence from blocks of five"""

        #The first one to be removed from the front is how many to del
        # from the end, the second is how many to pop() into a list 
        #these are the space indexes.
        for_indexes = list(enumerate("abcdefghijklmnopqrstuvwxyzABCDEF"
               "GHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-`~\|]}[{';:/?.>,<"))
        y = list(enumerate(x)) 
        w = "abcdefghijklmnopqrstuvwxyz"
        z = list(enumerate(w))
        x = x.replace(" ", "")
        x = list(x)
        del_from_end = x.pop(0)
        for a, b in z:
            if del_from_end == b:
                del_from_end = a 
        while del_from_end:
            del x[-1]
            del_from_end -= 1
        index_length = x.pop(0)
        for a, b in z:
            if index_length == b:
                index_length = a 
        letter_indexes = []
        while index_length:
            letter_indexes.append(x.pop())
            index_length -=1
        number_indexes = []
        for i in letter_indexes:
            for a, b in for_indexes:
                if i == b:
                    number_indexes.append(a)
        number_indexes.sort()
        counter = 0
        for i in number_indexes:
            x.insert(i, " ")
        x = "".join(x)
        return x
