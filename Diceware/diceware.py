import re
dict = {}
with open("wordlist") as file:
        lines = file.readlines()
        for line in lines:
            key = line[:5]
            value = line[6:-1]
            dict[key]=value


while True:
    key = input("Numbers:")
    if(key=="0"):
        break
    if len(key)!=5:
        print("Please enter 5 numbers")
        continue
    if not re.match("^[1-6]+$",key):
        print("Invalid numbers")
        continue

    print(dict[key])
