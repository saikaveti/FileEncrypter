class RSA(object):
    def __init__(self, inputTextFile, outputTextFile):
        self.inputFile = inputTextFile
        self.outputFile = outputTextFile
        self.n = 0
        self.p = 0
        self.q = 0
        self.e = 0

    def number_from_letter(self, inputChar):
        outputNumber = 1
        if inputChar == 'a' or inputChar == 'A':
            outputNumber = 0
        elif inputChar == 'b' or inputChar == 'B':
            outputNumber = 1
        elif inputChar == 'c' or inputChar == 'C':
            outputNumber = 2
        elif inputChar == 'd' or inputChar == 'D':
            outputNumber = 3
        elif inputChar == 'e' or inputChar == 'E':
            outputNumber = 4
        elif inputChar == 'f' or inputChar == 'F':
            outputNumber = 5
        elif inputChar == 'g' or inputChar == 'G':
            outputNumber = 6
        elif inputChar == 'h' or inputChar == 'H':
            outputNumber = 7
        elif inputChar == 'i' or inputChar == 'I':
            outputNumber = 8
        elif inputChar == 'j' or inputChar == 'J':
            outputNumber = 9
        elif inputChar == 'k' or inputChar == 'K':
            outputNumber = 10
        elif inputChar == 'l' or inputChar == 'L':
            outputNumber = 11
        elif inputChar == 'm' or inputChar == 'M':
            outputNumber = 12
        elif inputChar == 'n' or inputChar == 'N':
            outputNumber = 13
        elif inputChar == 'o' or inputChar == 'O':
            outputNumber = 14
        elif inputChar == 'p' or inputChar == 'P':
            outputNumber = 15
        elif inputChar == 'q' or inputChar == 'Q':
            outputNumber = 16
        elif inputChar == 'r' or inputChar == 'R':
            outputNumber = 17
        elif inputChar == 's' or inputChar == 'S':
            outputNumber = 18
        elif inputChar == 't' or inputChar == 'T':
            outputNumber = 19
        elif inputChar == 'u' or inputChar == 'U':
            outputNumber = 20
        elif inputChar == 'v' or inputChar == 'V':
            outputNumber = 21
        elif inputChar == 'w' or inputChar == 'W':
            outputNumber = 22
        elif inputChar == 'x' or inputChar == 'X':
            outputNumber = 23
        elif inputChar == 'y' or inputChar == 'Y':
            outputNumber = 24
        elif inputChar == 'z' or inputChar == 'Z':
            outputNumber = 25
        return outputNumber

    def assign_public_key_values(self):
        self.p = int(input("Enter Value of P (Prime): "))
        self.q = int(input("Enter Value of Q (Prime): "))
        self.e = int(input("Enter a small value of e (Prime)"))
        self.n = self.p * self.q

    def sub_public_key(self):
        publicKey = []
        publicKey.append(self.p)
        publicKey.append(self.q)
        publicKey.append(self.e)
        publicKey.append(self.n)

        return publicKey

    def sub_private_key(self):
        publicKey = self.sub_public_key()

        p = publicKey[0]
        q = publicKey[1]
        e = publicKey[2]
        phi = (p-1)*(q-1)

        # Assuming value of k = 2
        k = 2

        d = (k*phi+1)/(e)

        return d

    def get_public_key(self):
        inputKey = self.sub_public_key()
        n = inputKey[3]
        e = inputKey[2]

        key = []
        key.append(n)
        key.append(e)

        return key

    def get_private_key(self):
        d = self.sub_private_key()

        return d

    def encrypt_single_word(self, word):
        convert = ''
        for c in word:
            num = ord(c)
            convert = convert + str(num)
        numConvert = int(convert)

        public_key = self.get_public_key()
        n = public_key[0]
        e = public_key[1]
        encryptedNum = pow(numConvert, e, n)
        encryptedStr = str(encryptedNum)

        return encryptedStr

    def rsa(self):
        self.assign_public_key_values()
        inputFileObject = open(self.inputFile, 'r')
        inputFileText = inputFileObject.read()
        outputFileObject = open(self.outputFile, 'w')
        for word in inputFileText.split():
            encrypt = self.encrypt_single_word(word)
            outputFileObject.write(encrypt + " ")
        outputFileObject.write("\nRSA Encryption Implemented")