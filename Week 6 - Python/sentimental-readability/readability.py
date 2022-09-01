def main():
    # Prompt the user for input
    text = input("Text: ")

    # Calculating letters
    letters = count_letters(text)

    # Calculating words
    words = count_words(text)

    # Calculating sentences
    sentences = count_sentences(text)

    # Coleman-Liau index
    L = letters / words * 100.0
    S = sentences / words * 100.0
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Print Grades
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade", int(index))


def count_letters(text):
    # Calculating letters
    letters = 0
    for i in range(len(text)):
        if text[i].lower() >= 'a' and text[i].lower() <= 'z':
            letters += 1
    return letters


def count_words(text):
    # Calculating words
    words = 1
    for i in range(len(text)):
        if text[i] == ' ':
            words += 1
    return words


def count_sentences(text):
    # Calculating sentences
    sentences = 0
    for i in range(len(text)):
        if text[i] in ['.', '!', '?']:
            sentences += 1
    return sentences


if __name__ == "__main__":
    main()