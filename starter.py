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

# Rename the project in the setup
lines_setup = []
with open('setup.py') as infile:
    for line in infile:
        line = line.replace('pyquickstart',sys.argv[1])
        lines_setup.append(line)
with open('setup.py', 'w') as outfile:
    for line in lines_setup:
        outfile.write(line)

# README
lines_setup = []
with open('README.md') as infile:
    for line in infile:
        line = line.replace('pyquickstart',sys.argv[1])
        lines_setup.append(line)
with open('README.md', 'w') as outfile:
    for line in lines_setup:
        outfile.write(line)

# Rename the directories
os.rename('pyquickstart',sys.argv[1])
os.rename(os.getcwd(),os.path.dirname(os.getcwd())+'/'+sys.argv[1])
os.chdir('../')
print("Your project is now properly quickstarted! It can be found under the name you used: \n\tcd <your_name>\n")
print("Some actions still have to be done,\n\t-Setup git by removing .git and using git init\n\t-Check the setup.py file\n\t-Configure your virtual environment using mkvirtualenv -a . <your_env_name>")

# Display final informations
# Git setup
# Setup.py check description, classifiers, keywords

# Remove this helper
os.remove(sys.argv[0])
