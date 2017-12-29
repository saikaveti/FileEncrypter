class Vignere(object):

    def __init__(self, inputTextFile, outputTextFile, keyWordText):
        self.inputFile = inputTextFile
        self.outputFile = outputTextFile
        self.keyWord = keyWordText

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

    def letter_from_number(self, inputNumber):
        outputChar = 1
        if inputNumber == 0:
            outputChar = 'a'
        elif inputNumber == 1:
            outputChar = 'b'
        elif inputNumber == 2:
            outputChar = 'c'
        elif inputNumber == 3:
            outputChar = 'd'
        elif inputNumber == 4:
            outputChar = 'e'
        elif inputNumber == 5:
            outputChar = 'f'
        elif inputNumber == 6:
            outputChar = 'g'
        elif inputNumber == 7:
            outputChar = 'h'
        elif inputNumber == 8:
            outputChar = 'i'
        elif inputNumber == 9:
            outputChar = 'j'
        elif inputNumber == 10:
            outputChar = 'k'
        elif inputNumber == 11:
            outputChar = 'l'
        elif inputNumber == 12:
            outputChar = 'm'
        elif inputNumber == 13:
            outputChar = 'n'
        elif inputNumber == 14:
            outputChar = 'o'
        elif inputNumber == 15:
            outputChar = 'p'
        elif inputNumber == 16:
            outputChar = 'q'
        elif inputNumber == 17:
            outputChar = 'r'
        elif inputNumber == 18:
            outputChar = 's'
        elif inputNumber == 19:
            outputChar = 't'
        elif inputNumber == 20:
            outputChar = 'u'
        elif inputNumber == 21:
            outputChar = 'v'
        elif inputNumber == 22:
            outputChar = 'w'
        elif inputNumber == 23:
            outputChar = 'x'
        elif inputNumber == 24:
            outputChar = 'y'
        elif inputNumber == 25:
            outputChar = 'z'
        return outputChar

    def vignere_cipher(self):
        inputFileObject = open(self.inputFile)
        inputFileText = inputFileObject.read()
        keyword = self.keyWord
        keywordArray = list(keyword)
        inputFileArray = list(inputFileText)
        iterator = 0
        charCounter = 0
        outputFile = open(self.outputFile, "w")
        outputFile.write("Vignere Cipher Implemented\n")
        while (iterator < len(inputFileArray)):
            if inputFileArray[iterator].isalpha():
                inputNum = self.number_from_letter(inputFileArray[iterator])
                keywordIndex = charCounter % len(keywordArray)
                keywordNumber = self.number_from_letter(keywordArray[keywordIndex])
                finalNumber = (inputNum + keywordNumber) % 26
                finalLetter = self.letter_from_number(finalNumber)
                outputFile.write(finalLetter)
                iterator += 1
                charCounter += 1
            else:
                outputFile.write(inputFileArray[iterator])
                iterator += 1

