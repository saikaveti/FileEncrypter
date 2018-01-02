class RC4(object):
    def __init__(self, inputTextFile, outputTextFile, keyWordText):
        self.inputFile = inputTextFile
        self.outputFile = outputTextFile
        self.keyWord = keyWordText

    def generateArrayS(self):
        s = range(256)
        return s

    def swap(self, s, i, j):
        temp = s[j]
        s[j] = s[i]
        s[i] = temp

    def ksa(self, key):
        keylength = len(key)
        s = list(range(256))
        i = 0
        j = 0
        while i < 256:
            j = (j + s[i] + ord(key[i % keylength])) % 256
            s[i], s[j] = s[j], s[i]
            i += 1
        return s

    def prga(self, S):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            yield S[(S[i] + S[j]) % 256]

    def rc4(self, key):
        char_cipher_array = []
        firstAlt = self.ksa(key)
        byteGen = self.prga(firstAlt)
        inputObject = open(self.inputFile, "r")
        inputText = inputObject.read()
        for char in inputText:
            byte = ord(char)
            cipher_byte = byte ^ next(byteGen)
            char_cipher_array.append(str(cipher_byte))
        output = ''.join(char_cipher_array)
        charArray = list(output)
        outputFileObject = open(self.outputFile, "w")
        for char in charArray:
            outputFileObject.write(char)
        outputFileObject.write("\nRC4 Cipher Implemented")