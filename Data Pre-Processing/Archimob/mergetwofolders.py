#!/usr/bin/env python

import subprocess as sbp
import os

path = './Audio_1'
fol = os.listdir(path)
p2 = './Audio_merged'

for i in fol:
    p1 = os.path.join(path,i)
    p3 = 'cp -r ' + p1 +' ' + p2+'/.'
    sbp.Popen(p3,shell=True)
    print('one more file merged')
print('all files merged - Done')


#Sources: (adapted from)
## Title: Merge two folders in python
## URL: https://stackoverflow.com/questions/49122623/merge-two-folders-in-python
## Last accessed: 05/07/2019
