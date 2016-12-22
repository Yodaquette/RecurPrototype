"""
    Andrew Goodman
    December 21, 2016

    Parse the database config file
"""
from configparser import ConfigParser

def parseDbConnection(filename = "modules/database/config.ini",section = "db"):
    """
        Parse the database connection parameters from the config file

        :param file: configuration file
        :param section: config file section pertaining to the database
        :return: a dictionary of database connection parameters
    """
    try:
        parser = ConfigParser()
        parser.read(filename)

        # Store the database config dictionary
        db = {}

        # Read the config section "db"
        if(parser.has_section(section)):
            items = parser.items(section)
            # Read each item
            for item in items:
                # print("item: {0}".format(item))
                db[item[0]] = item[1] # item[0] is the key ; item[1] is the value
        else:
            raise Exception("{0} not found in file {1}".format(section,filename))
    except Exception as e:
        print("DEBUG - exception occurred: {0}".format(str(e)))

    return db
