try:
    file = open("zadachi.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found!")
    file.close()