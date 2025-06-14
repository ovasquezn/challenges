def pig_it(string):
    string = string.split() # Split the string into words
    for i in range(len(string)):
        if string[i].isalpha(): # Check if the word is alphabetic
            string[i] = string[i][1:] + string[i][0] + 'ay' # Move the first letter to the end and add 'ay'
    return ' '.join(string)

# Example usage
print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !