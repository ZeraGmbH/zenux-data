from PrepareReadMeMD import PrepareReadMeMD
import os
import argparse
import json
import sys

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ZenuxVersion', type=str, required=True, help='')
    parser.add_argument('--SessionNamesJson', type=str, required=True, help='')
    args = parser.parse_args()
    return args

def markdownSpecialChars():
    return ["*", "**", ">", "- ", "# ", "## ", "### "]

def renameDictKeys(originalDict, searchStr, replacementStr):
    renamedDict = dict()
    for key,value in originalDict.items():
        renamedDict[key.replace(searchStr, replacementStr)] = value
    return renamedDict

def escapeMDSpecialChars(map):
    for key in map :
        for specialChar in markdownSpecialChars() :
            escapeChar = "\\" + specialChar
            map[key] = map[key].replace(specialChar, escapeChar)
    return map

def parseSessionNamesJson(jsonFile):
    sessionNamesMap = json.load(open(jsonFile))
    mtmap = renameDictKeys(sessionNamesMap["mt310s2"], "json", "html")
    commap = renameDictKeys(sessionNamesMap["com5003"], "json", "html")
    mtmap = escapeMDSpecialChars(mtmap)
    commap = escapeMDSpecialChars(commap)
    return mtmap, commap


parent_directory = os.path.abspath('..')
sys.path.append(parent_directory)

args = parseArguments();
mtmap, commap = parseSessionNamesJson(args.SessionNamesJson)

newReadMe = PrepareReadMeMD('NEW_README.md')
newReadMe.addDeviceSessions("MT310s2", mtmap)
newReadMe.addDeviceSessions("COM5003", commap)
newReadMe.addPreviousVersions('README.md', args.ZenuxVersion)
newReadMe.createFile()

os.remove("README.md")
os.rename("NEW_README.md", "README.md")