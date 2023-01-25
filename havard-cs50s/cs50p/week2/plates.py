def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalnum(): # check if there is not punctuation
        if 2 <= len(s) <= 6: # validates lenght
            if s[:2].isalpha(): # validate 2 first digits to be alpha
                if s[:-1].isalpha(): # passing if all characters are alpha
                    return True

                for i in range(len(s)):
                    if s[i].isalpha():
                        continue
                    else:
                        if s[i] != '0' and s[i:-1].isdigit(): # if its not zero, check if last two are decimals
                            return True
                        else:
                            return False

main()