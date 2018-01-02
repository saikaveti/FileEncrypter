import random as rand

class ElGamal(object):
    def __init__(self, inputTextFile, outputTextFile):
        self.inputFile = inputTextFile
        self.outputFile = outputTextFile
        self.X = 0

    def bob_public_key(self):

        # Input P Value
        P = int(input("Enter Value of P: "))
        # Generate G Value
        G = rand.randint(1, P)
        # Generate X Value
        X = rand.randint(10, 210)
        self.X = X
        # Compute Y Value
        Y = pow(G, X, P)

        publicKey = []
        publicKey.append(P)
        publicKey.append(G)
        publicKey.append(Y)

        return publicKey

    def get_bob_x(self):
        return self.X


    def alice_encryption(self, message, public_key):

        # Retrieve P, G, and Y values
        P = public_key[0]
        G = public_key[1]
        Y = public_key[2]

        # Generate the private K value
        K = rand.randint(10, 210)

        A = pow(G, K, P)
        B = (pow(Y, K) * message) % P

        a_and_b = []
        a_and_b.append(A)
        a_and_b.append(B)

        return a_and_b

    def ElGamal(self):
        inputFileObject = open(self.inputFile)
        inputFileText = inputFileObject.read()
        message = int(inputFileText)
        publicKey = self.bob_public_key()
        a_and_b = self.alice_encryption(message, publicKey)
        outputFileObject = open(self.outputFile, "w")
        output_str = "A: " + str(a_and_b[0]) + ". B: " + str(a_and_b[1]) + "."
        outputFileObject.write(output_str)
        outputFileObject.write("\nEl Gamal Implemented")
