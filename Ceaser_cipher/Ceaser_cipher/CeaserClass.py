class Ceaser():

    def __init__(self,key,antiKey) -> None:
        self.key = key
        self.antiKey = antiKey


    #that function used to encrypt or decrypt msg basd on flag
    def process_str(self,msg,flag):
        self.check_input(msg)
        newstr = ''

        if flag:# if flag is true encrypt
            for letter in msg:
                newstr += self.key[letter]

        else:
            for letter in msg:
                newstr += self.antiKey[letter]


        return newstr
    
    def check_input(self,msg):
        alphabet_list = list(map(chr, range(97, 123)))
        alphabet_list.append(' ')

        for char in msg:
            if char not in alphabet_list:
                raise ValueError("it's not valid input, only alphabets and spaces allowed.")
    

