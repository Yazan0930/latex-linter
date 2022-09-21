
def addTaps(text):
    # check if starts with \t
    if text[0] == "\t":
        return text
    else:
        return "\t" + text

def breakUpSentences(line, newLine = "\n"):
    listOfSigns = [":", ";", ",", ".", "!", "?"]
    for i in listOfSigns:
        if i in line:
            index = line.index(i)
            if line[index+1:index+3] != newLine[:1] and i+i != line[-3: -1]:
                line = line.replace(i, i + newLine)
    return line

def addNewLines(line, number = 0):
    return (number * "\n") + line

def linterLatex(f, betterGitSupport, lineBreakSize):
    finalText = "" # final text to be written to file
    begin = ""
    lines = 0

    for line in f:
        if "begin{" in line and "document" not in line or begin != "":
            begin = line
            if "begin{" not in line and "end{" not in line:
                line = addTaps(line)
                if betterGitSupport is True:
                    finalText += breakUpSentences(line, "\n\t")
                else:
                    finalText += line
            else:
                finalText += line
            if "end{" in line:
                begin = ""


        elif betterGitSupport is True and "\\" != line[0] and "%" != line[0] and line != "\n":
            finalText += breakUpSentences(line, "\n")

        elif "%" == line[0]:
            finalText += line.replace("%", "% ")

        elif "\\" == line[0] and lines < lineBreakSize:
            n = len(finalText)
            for i in range(0, len(finalText)):
                if finalText[-1-i:n] == "\n":
                    lines += 1
                    n -= 1
                else:
                    break

            if lines-1 < lineBreakSize:
                finalText += addNewLines(line, (lineBreakSize))
            elif lines-1 > lineBreakSize:
                endIndex = len(finalText) - (lines-1 - lineBreakSize)
                finalText = finalText[:endIndex]
                finalText += line
            else:
                finalText += line
            lines = 0

        else:
            finalText += line
    return finalText
