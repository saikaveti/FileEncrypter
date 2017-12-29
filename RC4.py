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
        

    def rc4(self, key):
        s = self.generateArrayS()
        firstAlt = self.ksa(key)
        encrypt = self.prga(firstAlt)
        print(encrypt)