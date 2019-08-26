def messageWithWelcom(str):

    def addWelcome():
        return "Welcome to"

    return addWelcome() + str

def siteName(site_name):
    return site_name

print(messageWithWelcom(siteName("bishow")))