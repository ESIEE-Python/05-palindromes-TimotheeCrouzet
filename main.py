def remove_ponctuation(s):
    """On supprime la ponctuation d'une phrase
    Args:
        s : chaine de caractère
    Returns:
        s : chaine de caractère
    >>> remove_ponctuations(L'important, c'est d'aimer)
    limoportantcestdaimer
    """
    ponctuations = "?!,:. '-"
    for i in range(len(ponctuations)):
        s = s.replace(ponctuations[i], "")
    return s

def remove_accents(s):
    """On change la grammaire d'une phrase en enlevant les accents
    Args:
        s : chaine de caractère
    Returns:
        s : chaine de caractère
    >>> remove_accents(mariée)
    mariee
    """ 
    accents = "éëêèàùîôûç"
    sans_accents = "eeeeauioouc"
    for i in range(len(accents)):
        s = s.replace(accents[i], sans_accents[i])
    return s


def ispalindrome(s):
    """
    on cherche si un mot est un palindrome ou non. 
    Autrement dit, si on peut le lire à l'envers.
    Args:
        s : chaine de caractère
    Returns:
        True or False
    >>> ispalindrome(kayak)
    True
    >>> ispalindrome(manger)
    False
    """
    a = s.lower()
    a = remove_accents(remove_ponctuation((a)))
    b = a[::-1]
    if a == b :
        return True
    return False


def main():
    """créer notre module"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
