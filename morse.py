alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
morseAlpha = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', ' -.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']   


word = input("Input a word: ")
length = len(word)

morse = ''
for i in range(0, length):
    morse = (morse + (morseAlpha[alpha.index(word[i])]))

print(morse)
