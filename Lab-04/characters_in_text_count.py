text = input("Enter text: ")

dic = dict()

for character in text:
    if character in dic:
        dic[character] += 1
    else:
        dic[character] = 1

print(dic)
