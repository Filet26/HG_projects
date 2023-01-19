# Returns a txt file of unique apps based on input application file
# quick python implementation, next step is to make it a powershell program

import xml.etree.ElementTree as ET
import time
import sys

# Ask for file name / path and open file
# file_name = input('Enter file name/full path: ')


def parse_XML(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    return root

    
def parseApplications(root):
    # returns a list of applications
    apps = []

    # for each application
    for child in root:
        # print applicaton name contents
        apps.append(child[1].text)

    return apps

def writeToFiles(apps):
    pass


def main():
    try:
        # original filename 
        old_programs_file = sys.argv[1]
        old_program_tree = parse_XML(old_programs_file)
        # return count of apps in old computer
        time.sleep(0.5)
        print("There are " + str(len(old_program_tree)) + f" applications in the old computer -- {old_programs_file}.")
        print(70*"=")
        old_programs_list = parseApplications(old_program_tree)
        time.sleep(0.5)
        print("Old programs Parsed!")

    except:
        print("An Error Occured, Please check file names (old computer)")
        print("Usage: python unique_apps.py <old_computer_programs.xml> <new_computer_programs.xml>")
        sys.exit()

    try:
        # new computer programs filename
        new_programs_file = sys.argv[2]
        new_program_tree = parse_XML(new_programs_file)
        # return count of apps in old computer
        time.sleep(0.5)
        print("There are " + str(len(new_program_tree)) + f" applications in the new computer -- {new_programs_file}.")
        print(70*"=")
        new_programs_list = parseApplications(new_program_tree)
        time.sleep(0.5)
        print("New programs Parsed!")

    except:
        print("An Error Occured, Please check file names (new computer)")
        print("Usage: python unique_apps.py <old_computer_programs.xml> <new_computer_programs.xml>")
        sys.exit()
    
    # create a list of unique apps
    unique_apps = []

    # for each app in old computer
    for app in old_programs_list:
        # if app is not in new computer
        if app not in new_programs_list:
            # add app to unique apps list
            unique_apps.append(app)

    # print unique apps
    print("Unique apps: ")
    for app in unique_apps:
        print(app)

    print(70*"=")
    time.sleep(0.5)

    # print num of unique apps
    print("There are " + str(len(unique_apps)) + " unique applications.")

if __name__ == "__main__":
    main()




