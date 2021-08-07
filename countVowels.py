def vowels(string):
    for i in string:
        v = 0
        if (i == 'a'or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
    return v

string = input("\nEnter a word : ")

vowels = 0
consonants = 0
number_of_letters = 0

for i in string:
    number_of_letters = number_of_letters + 1
    if (i == 'a'or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1

    if (i == '.' or i == ' ' or i == '!' or i == '@' or i == '#' or i == '%' or i == '$' or i == '^' or i == '&' or i == '*' or i == '-' or i == '+' or i == '/'):
        number_of_letters = number_of_letters - 1

    if (i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
        number_of_letters = number_of_letters - 1

consonants = number_of_letters - vowels

print("The number of letters in the word are : ", number_of_letters)
print("The number of Vowels are : ", vowels)
print("The number of consonants are : ", consonants)