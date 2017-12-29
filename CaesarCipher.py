class Caesar(object):

    def __init__(self, inputTextFile, outputTextFile):
        self.inputFile = inputTextFile
        self.outputFile = outputTextFile

    def replace_letter(self, inputChar):
        tempChar = 'a'
        if inputChar == 'a' or inputChar == 'A':
            tempChar = 'd'
        elif inputChar == 'b' or inputChar == 'B':
            tempChar = 'e'
        elif inputChar == 'c' or inputChar == 'C':
            tempChar = 'f'
        elif inputChar == 'd' or inputChar == 'D':
            tempChar = 'g'
        elif inputChar == 'e' or inputChar == 'E':
            tempChar = 'h'
        elif inputChar == 'f' or inputChar == 'F':
            tempChar = 'i'
        elif inputChar == 'g' or inputChar == 'G':
            tempChar = 'j'
        elif inputChar == 'h' or inputChar == 'H':
            tempChar = 'k'
        elif inputChar == 'i' or inputChar == 'I':
            tempChar = 'l'
        elif inputChar == 'j' or inputChar == 'J':
            tempChar = 'm'
        elif inputChar == 'k' or inputChar == 'K':
            tempChar = 'n'
        elif inputChar == 'l' or inputChar == 'L':
            tempChar = 'o'
        elif inputChar == 'm' or inputChar == 'M':
            tempChar = 'p'
        elif inputChar == 'n' or inputChar == 'N':
            tempChar = 'q'
        elif inputChar == 'o' or inputChar == 'O':
            tempChar = 'r'
        elif inputChar == 'p' or inputChar == 'P':
            tempChar = 's'
        elif inputChar == 'q' or inputChar == 'Q':
            tempChar = 't'
        elif inputChar == 'r' or inputChar == 'R':
            tempChar = 'u'
        elif inputChar == 's' or inputChar == 'S':
            tempChar = 'v'
        elif inputChar == 't' or inputChar == 'T':
            tempChar = 'w'
        elif inputChar == 'u' or inputChar == 'U':
            tempChar = 'x'
        elif inputChar == 'v' or inputChar == 'V':
            tempChar = 'y'
        elif inputChar == 'w' or inputChar == 'W':
            tempChar = 'z'
        elif inputChar == 'x' or inputChar == 'X':
            tempChar = 'a'
        elif inputChar == 'y' or inputChar == 'Y':
            tempChar = 'b'
        elif inputChar == 'z' or inputChar == 'Z':
            tempChar = 'c'
        return tempChar

    def caesar_cipher(self):
        inputFileObject = open(self.inputFile, "r")
        inputFileText = inputFileObject.read()
        charArray = list(inputFileText)
        for index, char in enumerate(charArray):
            if char.isalpha():
                charArray[index] = self.replace_letter(char)
        outputFile = open(self.outputFile, "w")
        outputFile.write("Caesar Cipher Implemented\n")
        for char in charArray:
            outputFile.write(char)
