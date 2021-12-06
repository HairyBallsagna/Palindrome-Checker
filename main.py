def contains_multiple_words(string):
    return len(string.split()) > 1


def is_palindrome(sentence):
    if contains_multiple_words(sentence):
        string = "".join([val for val in sentence if str(val).isalnum()])
        return string[::-1].casefold() == string.casefold()
    else:
        return sentence[::-1].casefold() == sentence.casefold()


user_input = input("Please enter a word to check: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome")
else:
    print(f"'{user_input}' is not a palindrome")
