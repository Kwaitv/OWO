import pyperclip
import time
import os

def UWU(string):
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
                  "unto"   : "untwu",
                  "to"     : "tuwu",
                  "untrue" : "untwu",
                  'knew'   : 'knuwu',
                  'know'   : 'knowo',
                  'so'     : 'sho',
                  'no'     : 'nowo',

                }
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

def OWO_string(phrase):
    e = UWU(phrase)
    print(e)
    pyperclip.copy(e)


if __name__ == '__main__':
    OWO_string(input("phrase pls\n"))