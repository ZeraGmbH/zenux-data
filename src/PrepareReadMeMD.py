from mdutils.mdutils import MdUtils

def getPreviousVersionsHeading():
    return "Previous versions"

def getGithubPagesBaseUrl():
    return 'https://ZeraGmbH.github.io/zenux-data/scpi-documentation/'

class PrepareReadMeMD:
    
    def __init__(self, name):
        self.readMe = MdUtils(file_name=name, title='zenux-data')
        self.readMe.write(MdUtils(file_name='').read_md_file('BaseReadMe.md'))

    def addDeviceSessions(self, device, sessionDict):
        self.readMe.new_header(level=3, title=device, add_table_of_contents="n")
        for i in sessionDict :
            self.readMe.new_line('- ' + self.readMe.new_inline_link(link = getGithubPagesBaseUrl()+i, text = sessionDict[i]+' session'))

    def addPreviousVersions(self, oldReadMeFile, newVersion):
        oldReadMeContents = MdUtils(file_name='').read_md_file(oldReadMeFile)
        self.readMe.new_header(level=3, title=getPreviousVersionsHeading(), add_table_of_contents="n")
        self.readMe.write(oldReadMeContents.split(getPreviousVersionsHeading())[1])
        self.readMe.new_line('- ' + self.readMe.new_inline_link(link = getGithubPagesBaseUrl()+'archive/'+newVersion+'.tar.xz', text = newVersion))

    def createFile(self):
        self.readMe.create_md_file()

