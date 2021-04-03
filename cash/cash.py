import re


def main():
    cash = get_change()
    cash = cash*100
    counter = 0
    while cash > 0:
        if cash >= 25:
            cash = cash - 25
            counter += 1
        elif cash >= 10 and cash < 25:
            cash = cash - 10
            counter += 1
        elif cash >= 5 and cash < 10:
            cash = cash - 5
            counter += 1
        else:
            cash = cash - 1
            counter += 1

    print(counter)


def get_change():
    while True:
        change = input("Change owed: ")
        if change.isalpha():
            continue
        if change.isnumeric() or re.search(".", change):
            if float(change) > 0:
                break

    return float(change)


main()