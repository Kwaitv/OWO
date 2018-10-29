import pyperclip
import time
import os
#responses
def ask(string, truth):
    #truth is a string
    while True:
        mode = input(string + "\n").lower()

        if mode in truth.split() or mode == '':

            return mode
        else:
            continue

#converts pasted strings
def OWO_string(phrase):
    e = UWU(phrase)
    print(e)
    pyperclip.copy(e)

#conerts files
def OWO_file():
    #takes original file and starts making it owo
    gei = input("File Name: ")
    file = open(gei+".txt", "r")
    new_file = open('OWO_'+ gei + '.txt', "w")



    #writes owo file
    for line in file:
        e = UWU(line)
        new_file.write(e+ "\n")

    print(str(os.path.getsize(gei+".txt")) +" bytes")
    new_file.close()
def UWU(string):
    e = ''
    r = string.split()
    for word in r:
        if word.lower() in replace_s:
            if word.isupper():
                e += replace_s[word.lower()].capitalize()
            else:
                e += replace_s[word.lower()]
            e += " "
        else:
            for characters in word:
                if characters.lower() in replace:
                    if characters.isupper():
                        e += "W"
                    else:
                        e += "w"
                else:
                    e += characters
            e += " "
    if e.endswith(" "):
        e = e[:-1]
    return e

#scalable part
replace = ["r", "l"]

#custom replacement
replace_s =  {"you"    : "yuwu",
              "god"    : "gowod",
              "and"    : "awnd",
              "the"    : "teh",
              "that"   : "thawt",
              "be"     : "bwe",
              "man"    : "mawn",
              "serpent": "sewpwent",
              "unto"   : "untu",
              "to"     : "tuwu",
              "untrue" : "untwu"
              }

#decision
print("prerequisites for file conversion: \n - must be in the same folder \n - must be a .txt file\n\nalternative being phrase conversion \nwhich will ask you for a phrase \nand it will copy to your clipboard \nso all you need to do is paste")
p = ask("do you want to convert a file?","yes y no n")
if p in "yes y".split():
    r = time.time()
    OWO_file()
    e = time.time()
    print("Done in {} seconds".format(e-r))
else:
    OWO_string(input("phrase pls\n"))
