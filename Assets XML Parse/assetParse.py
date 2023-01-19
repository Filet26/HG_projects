#  Parses an XML file from lansweeeper to extract the asset information

import xml.etree.ElementTree as ET

tree = ET.parse("Assets_XML_files/computers.xml")

root = tree.getroot()

OS, Manufacturer, Model, SerialNumber = [], [], [], []

for child in root:
    OS.append(child[5].text)
    Manufacturer.append(child[6].text)
    Model.append(child[7].text)
    SerialNumber.append(child[26].text)

# get unique values

OS = list(set(OS))
Manufacturer = list(set(Manufacturer))
Model = list(set(Model))
SerialNumber = list(set(SerialNumber))

# print results

print("OS: ", OS)
# print("Manufacturer: ", Manufacturer)
# print("Model: ", Model)
# print("SerialNumber: ", SerialNumber)





    


