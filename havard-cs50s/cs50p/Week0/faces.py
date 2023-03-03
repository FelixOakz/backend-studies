def main():
    user = input()
    convert(user)


def convert(user):
    user = user.replace(':)', '🙂')
    user = user.replace(':(', '🙁')
    print(user)


main()
