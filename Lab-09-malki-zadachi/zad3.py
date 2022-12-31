binary_file = open("document.bin", "wb+")

text = "This is good"
encoded = text.encode("utf-8")
binary_file.write(encoded)
binary_file.seek(0)
binary_data = binary_file.read()
print("Binary:", binary_data)
text = binary_data.decode("ascii")
result = ""
for char in text:
    result += str(ord(char))
print("Decoded data:", result)

