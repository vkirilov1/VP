num = int(input("Enter number: "))

num_list = []
num_dic = dict()

for i in range(1, num+1):
    num_list.append(i)

reversed_list = num_list[::-1]

for i in range(0, len(num_list)):
    num_dic[num_list[i]] = reversed_list[i]

print(num_dic)