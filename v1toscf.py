import json
import csv

fileHeader = ["user", "pwd"]

csvFile = open("users.csv", "w")
writer = csv.writer(csvFile)
writer.writerow(fileHeader)

with open("user.json", "r") as fw:
    user_dict = json.load(fw)
    ct1 = 1
    while ct1 - 1 < len(user_dict):
        n = 1
        while n < len(user_dict[str(ct1)]):
            u = user_dict[str(ct1)][str(n)]["un"]
            p = user_dict[str(ct1)][str(n)]["pw"]
            print(u, p)
            add_info = [u, p]
            writer.writerow(add_info)
            n += 1
        ct1 += 1
