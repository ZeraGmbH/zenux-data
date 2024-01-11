import os
import sys
import json
from mdutils.mdutils import MdUtils

jsonFile = sys.argv[2]
sessionNamesMap = json.load(open(jsonFile))
mtmap = sessionNamesMap["mt310s2"]
commap = sessionNamesMap["com5003"]
mdSpecialSyntax = ["*", "**", ">", "- ", "# ", "## ", "### "]

mtmap = {key.replace("json", "html"):value for key,value in mtmap.items()}
commap = {key.replace("json", "html"):value for key,value in commap.items()}


for session in mtmap :
    for specialChar in mdSpecialSyntax :
        escapeChar = "\\" + specialChar
        mtmap[session] = mtmap[session].replace(specialChar, escapeChar)

for session in commap :
    for specialChar in mdSpecialSyntax :
        escapeChar = "\\" + specialChar
        commap[session] = commap[session].replace(specialChar, escapeChar)

#Recreate from title to 'Previous versions'
newReadMe = MdUtils(file_name='NEW_README.md',title='zenux-data')

newReadMe.new_paragraph("This is a set of documents describing SCPI interface on MT310s2 and COM5003 devices.")
newReadMe.new_header(level=2, title='SCPI Interface Descriptions', add_table_of_contents="n")

newReadMe.new_paragraph("Given below are links to the most recent versions of these documents:")

newReadMe.new_header(level=3, title='MT310s2', add_table_of_contents="n")
for i in mtmap :
    newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/' + i, text=mtmap[i] + ' session'))

newReadMe.new_header(level=3, title='COM5003', add_table_of_contents="n")
for i in commap :
    newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/' + i, text=commap[i] + ' session'))

newReadMe.new_header(level=3, title='Previous versions', add_table_of_contents="n")

#Take existing list under 'Previous versions'
oldReadMe = MdUtils(file_name='README.md',title='zenux-data')
oldReadMeContents = oldReadMe.read_md_file('README.md')
newReadMe.write(oldReadMeContents.split("### Previous versions")[1])

version = sys.argv[1]
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://zeragmbh.github.io/zenux-data/scpi-documentation/archive/' + version + '.tar.xz', text=version))
newReadMe.create_md_file()

os.remove("README.md")
os.rename("NEW_README.md", "README.md")
