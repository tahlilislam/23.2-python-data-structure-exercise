def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return phrase.title()

#Using split, capitalize and join

# phrase = "hello world"
# capitalized_phrase = ' '.join([word.capitalize() for word in phrase.split()])
# print(capitalized_phrase)  # "Hello World"

# #phrase = "hello world"
# words = phrase.split()
# capitalized_words = [word.capitalize() for word in words]
# capitalized_phrase = ' '.join(capitalized_words)
# print(capitalized_phrase)  # "Hello World"
