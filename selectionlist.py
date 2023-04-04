from bs4 import BeautifulSoup
import csv
import sys
#check for command line argument and open file if present else exit program

if len(sys.argv) != 2:
    print("Usage: %s '?export.xml?'" % sys.argv[0])
    sys.exit(1)

fd = open(sys.argv[1], 'r')
#fd open xml from command line argument
xml_file = fd.read()
soup = BeautifulSoup(xml_file, 'xml')
#iterate through xml file and get quanity from ItemQuanity and part number from PartName
filename = "book1.csv" #csv output file
with open(filename, "w",  newline='') as f:
    writer = csv.writer(f)
    #writer.writerow(["Qu:", "Part Number:"])
    #print("Qu:" , "Part Number: ") 
#    print("--------------------------------------------------")
    for child in soup.findAll("PartsPickListLine"):
        if child.find("ItemQuantity"):
            child.find("ItemQuantity").text
            child.find("PartName").text
#            child.find("PartItemDescription").text
            writer.writerows([(child.find('PartName').text, child.find('ItemQuanity').text)]) #partnumb,qu
#Quan, num            writer.writerows([(child.find("ItemQuantity").text, child.find("PartName").text)])
#            print(child.find("ItemQuantity").text, child.find("PartName").text)
fd.close()
