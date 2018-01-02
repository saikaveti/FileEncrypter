from CaesarCipher import *
from VignereCipher import *
from RC4 import *
from ElGamal import *

print("File Encryption Software:")
print("This software essentially serves to encrypt a certain text file")
print("The encrypted file's data will be written to a new text file")
print("Users will have the option of picking between different encryption types")

#inputTextFile = input("Enter file name: ")
inputTextFile = "SmallInput.txt"

#outputTextFile = input("Enter the file you want to write the encryption to:")
outputTextFile = "OutputFile.txt"

print("These are the algorithms currently implemented:")
print("Enter the number of the algorithm you want:")
print("1 - Caesar Cipher")
print("2 - Vignere Cipher")
print("3 - RC4 Cipher (Stream Cipher)")
print("4 - ElGamal Encryption")

choice = input("Enter Encryption Choice: ")

if (choice == "1"):
    caesarInputFileObject = Caesar(inputTextFile, outputTextFile)
    caesarInputFileObject.caesar_cipher()
    print("Caesar Cipher Complete. Verify by checking the output file")
elif (choice == "2"):
    vignereKeyword = input("Enter Keyword for Vignere Cipher:  ")
    vignereObject = Vignere(inputTextFile, outputTextFile, vignereKeyword)
    vignereObject.vignere_cipher()
    print("Vignere Cipher Complete. Verify by checking the output file")
elif (choice == "3"):
    RC4Keyword = input("Enter Keyword for RC4 Cipher:  ")
    rc4Object = RC4(inputTextFile, outputTextFile, RC4Keyword)
    rc4Object.rc4(RC4Keyword)
    print("RC4 Cipher Complete. Verify by checking the output file")
elif (choice == "4"):
    elGamObj = ElGamal(inputTextFile, outputTextFile)
    elGamObj.ElGamal()
    print("El Gamal Encryption Complete. Verify by checking the output file")

