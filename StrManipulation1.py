def checkpalindrome(inputstring):

    sas = inputstring[::-1]

    if (sas == inputstring):
        return True
    else:
        return False


print(checkpalindrome('asa'))


# Write a simple program that confirm if a string is a palindrome.