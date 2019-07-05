#This script will merge all textfiles from Archimob corpus to perform some nlp tasks

from glob import glob

with open('./merged.txt', 'w') as outfile:
    for file in glob('./Text in XML/*DE.txt'):
        print(file, 'done')
        with open(file) as infile:
            for line in infile:    #alternatively: outfile.write(infile.read())
                outfile.write(line)

print('Done')


#Sources: (adapted from)
## Title: Python concatenate text files
## URL: https://stackoverflow.com/questions/13613336/python-concatenate-text-files
## Last accessed: 05/07/2019
