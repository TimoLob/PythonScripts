import re
dict = {}
with open("wordlist") as file:
        lines = file.readlines()
        for line in lines:
            key = line[:5]
            value = line[6:-1]
            dict[key]=value


while True:
    print("Roll 5 dice and enter the numbers")
    key = input(">>>")
    if(key=="0"):
        break
    if len(key)!=5:
        print("Please enter 5 numbers")
        continue
    if not re.match("^[1-6]+$",key):
        print("Invalid numbers")
        continue

    print(dict[key])
