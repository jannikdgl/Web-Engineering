from tabulate import tabulate

def char_to_unicode(character):
    try:
        unicode_point = ord(character)
        return int(unicode_point)
    except TypeError:
        return "Ungültiges Zeichen"

with open('Eingabe.txt', 'r') as file:
    content = file.read()
    char_array = [char for char in content]

print(" -----------------------------------------------------------------------------------------------------------")
print("|   Encoding   |   Codepoint   |            Encoded Codepoint           |   Name of Character   |   Glyph   |")

data = []

for char in char_array:
    unicode_point = char_to_unicode(char)

    # Konvertiere den Unicode-Codepunkt in UTF-8 mit Little-Endian
    utf8_bytes = chr(unicode_point).encode('utf-8')

    # Konvertiere den Unicode-Codepunkt in UTF-16 mit Little-Endian
    utf16_bytes_be = chr(unicode_point).encode('utf-16be')

    # Konvertiere den Unicode-Codepunkt in UTF-16 mit Big-Endian
    #utf16_bytes_be = chr(unicode_point).encode('utf-16be')

    # Konvertiere den Unicode-Codepunkt in UTF-32 mit Big-Endian
    utf32_bytes_be = chr(unicode_point).encode('utf-32be')

    # Füge "Name of Character" und "Glyph" Informationen hinzu
    name_of_character = char
    glyph = char.encode('utf-8')

    data.extend([
        ["UTF-8", unicode_point, utf8_bytes.hex().upper(), glyph, name_of_character],
        ["UTF-16", unicode_point, utf16_bytes_be.hex().upper(), glyph, name_of_character],
        ["UTF-32", unicode_point, utf32_bytes_be.hex().upper(), glyph, name_of_character],
    ])

for row in data:
    print(
        f" -----------------------------------------------------------------------------------------------------------")
    print(f"|   {row[0]}      | {row[1]}         | {row[2]}            | {row[3]}                  | {row[4]} |")
    print(
        f" -----------------------------------------------------------------------------------------------------------")

print(tabulate(data, headers=["Encoding", "Codepoint", "Encoded Codepoint", "Name of Character", "Glyph"]))

