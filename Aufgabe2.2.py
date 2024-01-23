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
print("|   Encoding   |   Codepoint   |            Encoded Codepoint           |   Name of Character   |   Glyphe  |")

for char in char_array:
    unicode_point = char_to_unicode(char)

    # Konvertiere den Unicode-Codepunkt in UTF-8
    utf8 = chr(unicode_point).encode('utf-8')

    # Konvertiere den Unicode-Codepunkt in UTF-16 mit Little-Endian
    utf16_bytes_le = chr(unicode_point).encode('utf-16le')

    # Konvertiere den Unicode-Codepunkt in UTF-16 mit Big-Endian
    utf16_bytes_be = chr(unicode_point).encode('utf-16be')

    # Konvertiere den Unicode-Codepunkt in UTF-32 mit Big-Endian
    utf32_bytes_be = chr(unicode_point).encode('utf-32be')

    # Gib den UTF-16-Code auf der Konsole aus
    print(
        " -----------------------------------------------------------------------------------------------------------")
    print(f"|   UTF-8      | {hex(unicode_point)}         | {utf8}            |")

    print(" -----------------------------------------------------------------------------------------------------------")
    print(f"|   UTF-16 BE  | {hex(unicode_point)}         | {utf16_bytes_be.hex()}              |")
    print(
        " -----------------------------------------------------------------------------------------------------------")
    print(f"|   UTF-32 BE  | {hex(unicode_point)}         | {utf32_bytes_be.hex()}              |")
