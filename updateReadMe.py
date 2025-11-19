import os
import argparse
import json
from mdutils.mdutils import MdUtils

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

def sort_by_release_number(s):
    numb = (s.split('-')[1]).replace('.zip', '')
    return [int(c) for c in numb.split('.')]

def getArchiveEntries(dir):
    archives = list()
    for x in os.listdir(dir):
        if x.endswith(".zip"):
            archives.append(x)
    archivesSorted = sorted(archives, key=sort_by_release_number, reverse=True)
    return archivesSorted

args = parseArguments();

mtmap, commap = parseSessionNamesJson(args.SessionNamesJson)

#Recreate from title to 'Previous versions'
newReadMe = MdUtils(file_name='NEW_README.md',title='zenux-data')

newReadMe.new_paragraph("This is a set of documents describing SCPI interface on MT310s2 and COM5003 devices.")
newReadMe.new_line("These documents are created with operating system version: **" + args.ZenuxVersion + "**")
newReadMe.new_header(level=2, title='SCPI Interface Descriptions', add_table_of_contents="n")

newReadMe.new_paragraph("Given below are links to the most recent versions of these documents:")

newReadMe.new_header(level=3, title='MT310s2', add_table_of_contents="n")
for i in mtmap :
    newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/' + i, text=mtmap[i] + ' session'))
newReadMe.new_line('')

newReadMe.new_header(level=3, title='COM5003', add_table_of_contents="n")
for i in commap :
    newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/' + i, text=commap[i] + ' session'))
newReadMe.new_line('')

newReadMe.new_header(level=3, title='Change info', add_table_of_contents="n")
newReadMe.new_line('For details on changes in SCPI check ' +
                   newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/change-info.html', text='here') +
                   '.')
newReadMe.new_line('')

#'Previous versions'
newReadMe.new_header(level=3, title='Previous versions', add_table_of_contents="n")
newReadMe.new_line('Following are the links to previously archived versions. When clicked upon, a zip file will be downloaded.')
newReadMe.new_line('It is important to maintain the folder structure while unzipping this file.')
archives = getArchiveEntries("scpi-documentation/archive/")
for file in archives:
    releaseVersion = file.replace('.zip', '')
    newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://zeragmbh.github.io/zenux-data/scpi-documentation/archive/' + file, text=releaseVersion))
newReadMe.new_line('')

newReadMe.create_md_file()

os.remove("README.md")
os.rename("NEW_README.md", "README.md")
