# False Data Injection Attack on a simulated Air Traffic Controller

### Installation

I worked on the project through a virtual environment with `virtualenvwrapper`
and I highly recommend to do so as well. However, whether or not you are in a
virtual environment, the installation proceeds as follows:

* For downloading and installing the source code of the project:

  ```bash
    $ cd <directory you want to install to>
    $ git clone https://github.com/QDucasse/fdia_simulation
    $ python setup.py install
  ```
* For downloading and installing the source code of the project in a new virtual environment:  

  *Download of the source code & Creation of the virtual environment*
  ```bash
    $ cd <directory you want to install to>
    $ git clone https://github.com/QDucasse/fdia_simulation
    $ cd fdia_simulation
    $ mkvirtualenv -a . -r requirements.txt VIRTUALENV_NAME
  ```
  *Launch of the environment & installation of the project*
  ```bash
    $ workon VIRTUALENV_NAME
    $ pip install -e .
  ```

  *Launch of the basic GUI*
  ```bash
    $ python fdia_simulation/app.py
  ```
Note that the GUI does not contain all the features of the project but allows
you getting familiar with the components and interactions between them.  

---

### Structure of the project

Quick presentation of the different modules of the project:
* [**Package1:**][package]
Dynamic systems models.

---

### Requirements

This project uses five main libraries:
* [`Dependency1`][dependency1]

If installed as specified above, the requirements are stated in the ``requirements.txt`` file
and therefore automatically installed.  
However, you can install each of them separately with the command:
```bash
  $ pip install <library>
```


**NOTE:** *This project was created with Python 3.7.3 and no backward compatibility is
ensured.*  

---

### Objectives and Milestones of the project

- [X] Basic project structure
---

### Testing

All tests are written to work with `nose` and/or `pytest`. Just type `pytest` or
`nosetests` as a command line in the project. Every test file can still be launched
by executing the testfile itself.
```bash
  $ python PythonStarterProject/tests/chosentest.py
  $ pytest
```

---

### References

[package]:https://github.com/QDucasse/PythonStarterProject/tree/master/PythonStarterProject/package
[dependency1]: https://dependency1.com
