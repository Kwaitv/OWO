import pyperclip
import time
import os
from OWO_string import UWU

#responses
def ask(string, truth):
    #truth is a string
    while True:
        mode = input(string + "\n").lower()

        if mode in truth.split() or mode == '':

            return mode
        else:
            continue

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


if __name__ == "__main__":
    #decision
    print("prerequisites for file conversion: \n - must be in the same folder \n - must be a .txt file\n\nalternative being phrase conversion \nwhich will ask you for a phrase \nand it will copy to your clipboard \nso all you need to do is paste")

    r = time.time()
    OWO_file()
    
    print(UWU('gay'))
    e = time.time()
    print("Done in {} seconds".format(e-r))
