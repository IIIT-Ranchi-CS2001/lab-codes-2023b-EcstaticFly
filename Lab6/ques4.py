str=input("Enter String: ")
e=str.split(" ")
print(e)
uppercase_letters = list(
    map(lambda s: s.upper(), filter(lambda s: s.isalpha(), e))
)
squared_digits = list(
    map(lambda x: int(x)**2, filter(lambda s: s.isdigit(), e))
)
alphaNumeric=list(
    (filter(lambda s: s.isalnum(), e))
)
print(uppercase_letters)
print(squared_digits)
print(alphaNumeric)