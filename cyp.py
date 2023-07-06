import math

def encrypt(plainText, key):
    # Remove any spaces or special characters from the plaintext
    plainText = plainText.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")

    # Calculate the number of columns based on the key length
    numColumns = len(key)

    # Calculate the number of rows based on the plaintext length and number of columns
    numRows = math.ceil(len(plainText) / numColumns)

    # Pad the plaintext with extra characters to fill the last row if necessary
    paddedText = plainText.ljust(numRows * numColumns)

    # Create an empty matrix to hold the plaintext characters
    matrix = [[''] * numColumns for _ in range(numRows)]

    # Fill the matrix with the characters from the padded plaintext
    index = 0
    for row in range(numRows):
        for col in range(numColumns):
            matrix[row][col] = paddedText[index]
            index += 1

    # Create a list of column indices sorted according to the key
    sortedIndices = [i[0] for i in sorted(enumerate(key), key=lambda x: x[1])]

    # Build the cipher by reading the matrix column by column using the sorted indices
    cipher = ""
    for col in sortedIndices:
        for row in range(numRows):
            cipher += matrix[row][col]

    return cipher

def decrypt(cipher, key):
    # Calculate the number of columns based on the key length
    numColumns = len(key)

    # Calculate the number of rows based on the cipher length and number of columns
    numRows = math.ceil(len(cipher) / numColumns)

    # Create an empty matrix to hold the cipher characters
    matrix = [[''] * numColumns for _ in range(numRows)]

    # Calculate the number of characters in the last row
    numLastRowChars = numColumns - (numRows * numColumns - len(cipher))

    # Create a list of column indices sorted according to the key
    sortedIndices = [i[0] for i in sorted(enumerate(key), key=lambda x: x[1])]

    # Fill the matrix column by column using the sorted indices
    index = 0
    for col in sortedIndices:
        # Determine the number of characters to read for the current column
        numChars = numRows if col < numLastRowChars else numRows - 1

        # Fill the column with characters from the cipher
        for row in range(numChars):
            matrix[row][col] = cipher[index]
            index += 1

    # Build the plaintext by reading the matrix row by row
    plainText = ""
    for row in range(numRows):
        for col in range(numColumns):
            plainText += matrix[row][col]

    return plainText

plaintext = "Test One Two Three"
key = "hello"
