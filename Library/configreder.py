import configparser

def readConfigdata(section,key):
    config =configparser.ConfigParser()
    config.read("./ConfigurationFiles/config.cfg")
    return config.get(section,key)

def fetchelemnt(section,key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/elements.cfg")
    return config.get(section, key)

