from sys import argv
import csv
import re
import time


def main():
    # for invalid argumnets
    if len(argv) != 3:
        print("Error code")
        exit(1)
    text = open(argv[2], "r")
    string = text.read()
    with open(argv[1], "r") as csvfile:
        counter = 0
        spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)  # reading CSV file in a list
        x = next(spamreader)  # column headings of CSV file
        finallist = [] 
        for j in range(1, len(x)):
            substring = x[j]
            pattern = r'(?:'+substring+')+'
            groups = re.findall(pattern, string)
            if len(groups) == 0:
                print("no match")
                exit(1)
            largest = max(groups, key=len)
            finallist.append(len(largest)//len(x[j]))

        final = []
        for i in finallist:
            final.append(i)
        check = False
        for i in spamreader:
            checkList = i  # getting every row of CSV
            integerlist = checkList[1:len(checkList)]  # cextracting the list of SRT counts from the list 
            newintlist = []

            for j in integerlist:
                val = j
                newintlist.append(int(val))  # converting it to inttype
                if newintlist == final:  # comparing the list of CSV file and the list obtained from the sequence file
                    print(i[0])
                    check = True
                    break
        if check == False:
            print("No match") 
            exit(1)


main()