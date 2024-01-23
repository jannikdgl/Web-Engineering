def char_to_unicode(character):
    try:
        unicode_point = ord(character)
        return hex(unicode_point)
    except TypeError:
        return "Ungültiges Zeichen"



with open('Eingabe.txt', 'r') as file:
    content = file.read()
    char_array = [char for char in content]

result = char_to_unicode(content)
print(f"Der Unicode-Punkt für das Zeichen '{content}' ist: {result}")
