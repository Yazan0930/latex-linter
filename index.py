from pickle import TRUE
import sys
import json
import functions
from tabnanny import check


mage = r"""
                                88
                                88              ,d
                                88              88
                                88 ,adPPYYba, MM88MMM ,adPPYba, 8b,     ,d8
                                88 ""     `Y8   88   a8P_____88  `Y8, ,8P'
                                88 ,adPPPPP88   88   8PP"""""""    )888(
                                88 88,    ,88   88,  "8b,   ,aa  ,d8" "8b,
                                88 `"8bbdP"Y8   "Y888 `"Ybbd8"' 8P'     `Y8



"""


def main():
    jsonFile = open("config.json")
    jsonData = json.load(jsonFile)
    betterGitSupport = jsonData["betterGitSupport"]
    lineBreakSize = jsonData["lineBreakSize"]
    jsonFile.close()
    fileName = ""

    while(TRUE):
        print(f"""
            {mage}
            A) Enter a file name:

            B) Newline after a sentence for better git support:

            C) Blank lines before section, chapter, etc. (number adjustable):


                            D) START updates Latex file

            E) See the new file

            Q) End program

        """)
        choice = input("What do you want to do? ")
        if choice in "Aa":
            fileName = input("Enter the file name: ")
        elif choice in "Bb":
            betterGitSupport = not betterGitSupport
        elif choice in "Cc":
            lineBreakSize = int(input("Enter number of lines: "))
        elif choice in "Dd":
            if fileName == "":
                print("\nNo file selected")
            else:
                baseFile = open(fileName)
                finalText = functions.linterLatex(baseFile, betterGitSupport, lineBreakSize)
                newFile = open(f"Linter_{fileName}", "w")
                newFile.write(finalText)
                newFile.close()
                baseFile.close()
                print(f"\nUpdates are in the file Linter_{fileName}")
        elif choice in "Ee":
            print(finalText)
        elif choice in "Qq":
            print("\nBye, bye - and welcome back anytime!")
            break
        else:
            print("Invalid input")




if __name__ == "__main__":
    main()