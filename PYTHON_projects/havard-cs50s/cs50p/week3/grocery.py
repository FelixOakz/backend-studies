def main():
    grocery_list = user_input()
    sorted_dict = dict(sorted(grocery_list.items(),
                       key=lambda x: x[0].lower()))
    for k, v in sorted_dict.items():
        print(v, k)


def user_input():
    items = {}
    while True:
        try:
            item = input().upper()
            try:
                items.update({item: items[item]+1})
            except KeyError:
                items.update({item: 1})
        except EOFError:
            break
    return items


if __name__ == '__main__':
    main()
