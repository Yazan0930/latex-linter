#!/usr/local/bin/python3

import json


def startLintering(fileName):
    # check if file can be opened
    try:
        baseFile = open(fileName)
        # set Json Data in newLine and breakSentence
        newLine, breakSentence = setJsonData()
        finalText = linterLatex(baseFile, breakSentence, int(newLine))
        newFile = open(f"Linter_{fileName}", "w")
        newFile.write(finalText)
        newFile.close()
        baseFile.close()
        print(f"\nUpdates are in the file Linter_{fileName}")
    except:
        print("File not found ==> ", fileName)
        return


def addTaps(text, tabs):
    # check if starts with \t
    if text[0] == "\t":
        return text.replace("\t", tabs*"\t")
    else:
        return (tabs*"\t") + text

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

def addSpaceInComment(text):
    return text.replace("%", "% ")


def linterLatex(f, betterGitSupport, lineBreakSize):
    finalText = "" # final text to be written to file
    begin = ""
    lines = 0
    beginCounter = -1

    for line in f:
        if "begin{" in line and "{document" not in line or begin != "":
            if "begin{" in line:
                begin = line
                beginCounter += 1
                finalText += addTaps(line, beginCounter)
            elif "end{" in line:
                finalText += addTaps(line, beginCounter)
                beginCounter -= 1
                if  beginCounter == -1:
                    begin = ""
            else:
                if betterGitSupport is True:
                    line = breakUpSentences(line, "\n" + ("\t" * (beginCounter + 1)))
                    finalText += addTaps(line, beginCounter + 1)
                else:
                    finalText += addTaps(line, beginCounter + 1)

        elif betterGitSupport is True and "\\" != line[0] and "%" != line[0] and line != "\n":
            finalText += breakUpSentences(line, "\n")

        elif "%" == line[0]:
            finalText += addSpaceInComment(line)

        elif "\\" == line[0] and lines < lineBreakSize:
            n = len(finalText)
            for i in range(0, len(finalText)):
                if finalText[-1-i:n] == "\n":
                    lines += 1
                    n -= 1
                else:
                    break

            if lines-1 < lineBreakSize:
                finalText += addNewLines(line, (lineBreakSize - lines +1))

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



def updateConfig(jsonData, key, value):
    jsonData["custom"][key] = value
    jsonFile = open("$HOME/bin/latex-linter/config.json", "w")
    jsonFile.write(json.dumps(jsonData))
    jsonFile.close()

# get json data
def getJsonData():
    jsonFile = open("$HOME/bin/latex-linter/config.json")
    jsonData = json.load(jsonFile)
    jsonFile.close()
    return jsonData

# see if ther is a custom data in json file and get hte custom data
def setJsonData():
    jsonData = getJsonData()
    # check if there is not empty custom data
    if jsonData["custom"] != {}:
        # get the custom data
        if "newLine" in jsonData["custom"]:
            newLine = jsonData["custom"]["newLine"]
        else:
            newLine = jsonData["difault"]["newLine"]
        # if breakSentence in custom dictionary
        if "breakSentence" in jsonData["custom"]:
            breakSentence = jsonData["custom"]["breakSentence"]
        else:
            breakSentence = jsonData["difault"]["breakSentence"]
    else:
        newLine = jsonData["difault"]["newLine"]
        breakSentence = jsonData["difault"]["breakSentence"]

    return newLine, breakSentence


# chekc file type
def checkFileType(fileName):
    jsonData = getJsonData()
    # check if file type  is in json default values
    if fileName.split(".")[-1] in jsonData["difault"]["fileTypes"]:
        return True
    else:
        return False