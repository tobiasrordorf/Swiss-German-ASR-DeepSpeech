import os
import shutil

src = r'./audio'
dest = r'./merged'

for path, subdirs, files in os.walk(src):
    for name in files:
        filename = os.path.join(path, name)
        shutil.copy2(filename, dest)
print('Merge complete!')
