def palindrom(word):
    """
    Ta funkcja sprawdza, czy podany wyraz jest palindromem
    """
    word_2 = word[::-1]
    if word == word_2:
        return True
    else:
        return False


print(palindrom("kajak"))