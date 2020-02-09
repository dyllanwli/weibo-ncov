import os


id = []
all_id = []
for filename in os.listdir(os.getcwd()):
    with open(filename, "r") as file:
        all_id += file.readlines()


with open("../user_list.txt", "r") as file:
    for line in file.readlines():
        line = line.split(" ")
        id.append(line[0])


with open("user_id_list_non_duplicated.txt", "w") as file:
    id = set(id)
    id = id.difference(set(all_id))
    print(id)
    for i in list(id):
        line = str(i) + "\n"
        file.write(line)
    # file.writelines(list(id))