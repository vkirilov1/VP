text = input("Enter text: ")

characters = list(text)
dic = dict()

for character in characters:
    if character in dic:
        dic[character] += 1
    else:
        dic[character] = 1

print(dic)
