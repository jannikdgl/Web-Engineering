def char_to_unicode(character):
    try:
        unicode_point = ord(character)
        return hex(unicode_point)
    except TypeError:
        return "Ungültiges Zeichen"



with open('Eingabe.txt', 'r') as file:
    content = file.read()
    char_array = [char for char in content]

for char in char_array:
    result = char_to_unicode(char)
    print(f"Der Unicode-Punkt für das Zeichen '{char}' ist: {result}")
