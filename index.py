from pickle import TRUE
import functions
from tabnanny import check
import argparse

parser = argparse.ArgumentParser(description='Linter rols.')
parser.add_argument('-f', '--file', help='File to be linted')
parser.add_argument('-n', '--breakSentence', help='Newline after a sentence for better git support')
parser.add_argument('-l', '--lines', help='Blank lines before section, chapter, etc. (number adjustable)')
args = parser.parse_args()



def main():
    if args.file:
       functions.startLintering(args.file)
    elif args.breakSentence:
        # update jsonFile
        functions.updateConfig(functions.getJsonData(), "breakSentence", args.breakSentence)
        print(f"\nNewline after a sentence is now {args.breakSentence}")

    elif args.lines:
        functions.updateConfig(functions.getJsonData(), "newLine", args.lines)
        print(f"\nBlank lines before section, chapter, etc. is now {args.lines}")
    else:
        main()


if __name__ == "__main__":
    main()