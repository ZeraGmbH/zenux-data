import os
import sys
from mdutils.mdutils import MdUtils

#Recreate from title to 'Previous versions'
newReadMe = MdUtils(file_name='NEW_README.md',title='zenux-data')

newReadMe.new_paragraph("This is a set of documents describing SCPI interface on MT310s2 and COM5003 devices.")
newReadMe.new_header(level=2, title='SCPI Interface Descriptions', add_table_of_contents="n")

newReadMe.new_paragraph("Given below are links to the most recent versions of these documents:")

newReadMe.new_header(level=3, title='MT310s2', add_table_of_contents="n")
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/mt310s2-meas-session.html', text='Default Session'))
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/mt310s2-emob-session.html', text='EMOB AC/DC Session'))
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/mt310s2-emob-session-ac.html', text='EMOB AC Session')) 
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/mt310s2-emob-session-dc.html', text='EMOB DC Session')) 
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/mt310s2-dc-session.html', text='DC: 4\*Voltage / 1\*Current Session'))

newReadMe.new_header(level=3, title='COM5003', add_table_of_contents="n")
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/com5003-meas-session.html', text='Default Session'))
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/com5003-ced-session.html', text='Changing energy direction Session'))
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/com5003-ref-session.html', text='Reference Session')) 
newReadMe.new_line('- ' + newReadMe.new_inline_link(link='https://ZeraGmbH.github.io/zenux-data/scpi-documentation/com5003-perphase-session.html', text='3 Systems / 2 Wires Session'))

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
