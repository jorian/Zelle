__author__ = 'Jorian'
def ceasarscript():

    phrase = input("Please enter the phrase to encode: ")
    key = int(input("Please enter the key: "))
    totalphrase = "".join(phrase)

    encodedPhrase = ""
    for ch in totalphrase:
            if ord(ch) + key > (97+25):
                encodedPhrase = encodedPhrase + chr(ord(ch) + (key - 26))
            else: encodedPhrase = encodedPhrase + chr(ord(ch) + key)

    print(encodedPhrase)

    toDecodePhrase = input("Please enter the phrase to decode: ")
    decodedPhrase = ""
    for i in toDecodePhrase:
        decodedPhrase = decodedPhrase + chr(ord(i) + (key * -1))

    print(decodedPhrase)

ceasarscript()