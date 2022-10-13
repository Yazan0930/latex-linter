#!/usr/bin/env python3

import functions
# argparse library makes it easy to write user-friendly command-line interfaces.
import argparse


parser = argparse.ArgumentParser(description='Linter rols.')
parser.add_argument('-f', '--file', help='File to be linted')
parser.add_argument('-b', '--breakSentence', help='Newline after a sentence for better git support. Usage: -b [True/False]')
parser.add_argument('-l', '--lines', help='Blank lines before section, chapter, etc. (number adjustable). Usage: -l [number]')
args = parser.parse_args()


def main():

    if args.breakSentence:
        # update jsonFile
        if args.breakSentence == "True" or args.breakSentence == "true":
            functions.updateConfig(functions.getJsonData(), "breakSentence", True)
            print(f"\nNewline after a sentence is now {args.breakSentence}")
        elif args.breakSentence == "False" or args.breakSentence == "false":
            functions.updateConfig(functions.getJsonData(), "breakSentence", False)
            print(f"\nNewline after a sentence is now {args.breakSentence}")
        else:
            print("Invalid argument for breakSentence option (True/False)")

    if args.lines:
        # update jsonFile
        if args.lines.isdigit():
            functions.updateConfig(functions.getJsonData(), "newLine", int(args.lines))
            print(f"\nBlank lines before section, chapter, etc. is now {args.lines}")
        else:
            print("Invalid argument for lines option (number)")

    if args.file:
        if functions.checkFileType(args.file):
            functions.startLintering(args.file)
        else:
            print("File is not a (.tex or .bib or .tikz)  LaTex file type")
    # if args.file:
    #     fileName = args.file
    #     print("File to be linted: ", fileName)
    # if args.breakSentence:
    #     gitSoport = args.breakSentence
    #     print("Newline after a sentence for better git support: ", gitSoport)
    # if args.lines:
    #     amountLines = args.lines
    #     print("Blank lines before section, chapter, etc. (number adjustable): ", amountLines)



if __name__ == "__main__":
    main()

# python is the language that we are using to code the program, and if __name__ == "__main__": is a special code that allows you to execute the code in the main function.