import hashlib

secret = "34d5cf6ecc220ab4c31d90f41f07c9a1"

colors_file = open("wikicolorslower.txt","r")
goons_file = open("goons.txt","r")

colors = colors_file.readlines()
goons = goons_file.readlines()

m = hashlib.md5()

for y in range (1800,2500):
    for g in range (len(goons)):
        for c in range (len(colors)):
            password = str(y)+"-"+goons[g].rstrip("\n") +"-"+colors[c].rstrip("\n")
            #print(password)
            if hashlib.md5(password.encode("ascii")).hexdigest() == secret:
                print(password)
                exit()

colors_file.close()
goons_file.close()

