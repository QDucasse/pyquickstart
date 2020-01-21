# Python project structure and quickstart

### Intention

Having a clean project structure is essential to quality code development. By
cloning this repository and running a simple script, you can have a working environment
in matters of minutes!

### Quickstart your project!

Simply run the `starter.py` script from the root folder and provide a name to
your project in order for the script to reset the version control and refactor
`setup.py`, the `README` as well the name of the directories.

```bash
  $ git clone git@github.com:QDucasse/pyquickstart.git
  $ cd pyquickstart
  $ python starter.py
```

You can then create a new repository and link it to your new project by first
creating a new repository on Github then
```bash
  $ git remote add origin git@github.com:QDucasse/<repo name>.git
  $ git add .
  $ git commit -m "Initial commit"
  $ git push -u origin master
```

There it is, your repository is now set up!

Please check the different categories within the `setup.py` file and correct them
in accordance with your project. The categories description, classifiers and
keywords should be changing!
