# -*- coding: utf-8 -*-

# pyquickstart
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

import os
import sys
import datetime
import subprocess
from pathlib import Path

### LICENSE
with open('LICENSE') as infile:
    for i,line in enumerate(infile):
        if i==2:
            line.replace('2020',str(datetime.datetime.now().year))

### README INSTALLATION
os.remove('README.md')
os.rename('new_README.md','README.md')

# Rename all 'pyquickstart' to the provided name
for subdir, dirs, files in os.walk(os.getcwd()):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".py"):
            lines_setup = []
            with open(filepath) as infile:
                for line in infile:
                    line = line.replace('pyquickstart',sys.argv[1])
                    lines_setup.append(line)
            with open(filepath, 'w') as outfile:
                for line in lines_setup:
                    outfile.write(line)

# Rename the directories
os.rename('pyquickstart',sys.argv[1])
os.rename(os.getcwd(),os.path.dirname(os.getcwd())+'/'+sys.argv[1])
os.remove(sys.argv[0])
os.chdir('../')
print("Your project is now properly quickstarted! It can be found under the name you used: \n  cd <your_name>\n")
print("Some actions still have to be done,\n  -Setup git by removing .git and using git init\n  -Check the setup.py file\n  -Configure your virtual environment using mkvirtualenv -a . <your_env_name>")
