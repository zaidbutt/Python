from cs50 import get_string
import string


def main():
    text = get_string("Text: ")
    letters = 0
    words = 0
    sentences = 0
    for i in text:
        if (i in string.ascii_lowercase) or (i in string.ascii_uppercase):
            letters += 1
        elif i.isspace():
            words += 1
        elif i in ["!", ".", "?"]:
            sentences += 1
    # end for loop

    words += 1
    L = float(letters / words) * 100  # calculating letters per 100 words
    S = float(sentences / words) * 100  # calculating sentences per 100 words
    index = 0.0588 * L - 0.296 * S - 15.8
    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade %.0f" % index)


main()