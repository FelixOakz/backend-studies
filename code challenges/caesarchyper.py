s = 'middle-Outz'
k = 2


def caesarCipher(s, k):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for letter in s:
        if letter.isalpha():
            if letter.islower():
                loc = (alpha.find(letter) + k) % 26
                out += alpha[loc]
            else:
                letter = letter.lower()
                loc = (alpha.find(letter) + k) % 26
                out += alpha[loc].upper()
        else:
            out += letter
    print(out)

caesarCipher(s, k)
