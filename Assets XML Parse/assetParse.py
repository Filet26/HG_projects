#  Parses an XML file from lansweeeper to extract the asset information
import pandas as pd
import xml.etree.ElementTree as ET



def parseXML(xmlfile):
    tree = ET.parse(xmlfile)

    root = tree.getroot()

    OS, Manufacturer, Model, SerialNumber = [], [], [], []

    for child in root:
        OS.append(child[5].text)
        Manufacturer.append(child[6].text)
        Model.append(child[7].text)
        SerialNumber.append(child[26].text)

    return OS, Manufacturer, Model, SerialNumber




#  use pandas to create a dataframe



# export to excel

# df.to_excel("Output/computers.xlsx", index=False)


def main():
    OS, Manufacturer, Model, SerialNumber = parseXML("Assets_XML_files/computers.xml")
    
    OSSet, ManufacturerSet, ModelSet, SerialNumberSet = set(OS), set(Manufacturer), set(Model), set(SerialNumber)

    df = pd.DataFrame(list(zip(OS, Manufacturer, Model, SerialNumber)), columns =['OS', 'Manufacturer', 'Model', 'SerialNumber'])

    print(df)
    
    # print results

    # print("OS: ", OSSet)
    # print("Manufacturer: ", ManufacturerSet)
    # print("Model: ", ModelSet)
    # print("SerialNumber: ", SerialNumberSet)


    # count results

    # print("OS: ", len(OS))
    # print("Manufacturer: ", len(Manufacturer))
    # print("Model: ", len(Model))
    # print("SerialNumber: ", len(SerialNumber))

    pass


if __name__ == "__main__":
    main()



    


