#!/usr/bin/env python
# coding: utf-8

#This file helps retract the transcribed text of archimob audio from xml to txt
#Swiss German Text
#Source: https://www.datacamp.com/community/tutorials/python-xml-elementtree

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
