import os


id = []

with open("user_list.txt", "r") as file:
    for line in file.readlines():
        line = line.split(" ")
        id.append(line[1])


with open("user_list_warppered.txt", "w") as file:
    id = list(set(id))
    file.writelines(id)