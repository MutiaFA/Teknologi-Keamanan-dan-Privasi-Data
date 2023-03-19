alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "fcpevqkzgmtrayonujdlwhbxsi"
text = "nama saya mutia"

result = ""
for letter in text:
    if letter.lower() in alphabet:
        result += key[alphabet.find(letter.lower())]
    else:
        result += letter

print(result)
