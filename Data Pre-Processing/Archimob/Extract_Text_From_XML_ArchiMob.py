# File: Extract_Text_From_XML_ArchiMob.py for archimob data

#This file helps retract the transcribed text of archimob audio from xml to txt

#Import XML Reader
import xml.etree.ElementTree as ET
import pandas
from glob import glob

for entry in glob('./Text in XML/*.xml'):
    tree = ET.parse(entry)
    root = tree.getroot()
    txt_file = open(entry + '_DE.txt','w')

    for word in root.iter('{http://www.tei-c.org/ns/1.0}w'):
        text = word.attrib['normalised']     #either text for CH or attrib['normalised'] for DE
        text_new = text.split()
        for item in text_new:
            txt_file.write('%s\n' % item)
    print(entry + 'Done')

print('All Done!')


#Sources: (adapted from)
## Title: Python XML with ElementTree: Beginner's Guide
## URL: https://www.datacamp.com/community/tutorials/python-xml-elementtree
## Last accessed: 05/07/2019
