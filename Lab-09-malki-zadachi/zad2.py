file = open("info.txt", "r", encoding="utf-8")

for line in file:
    print(line)
file.close()