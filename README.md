# Library

It's a web application, created for educational purposes, for keeping records of your home book collection.

## Preparation

First, make sure you have the python (ver. 3.11.0) language interpreter installed. Then, go to library_project directory.

To ensure proper operation of the application, make sure that versions of the relevant modules are installed on the device, according to the requirements.txt file, which can be done with the following command (using the package manager [pip](https://pip.pypa.io/en/stable/)):

```bash
pip install -r requirements.txt
```

Next, create a local database compatible with the last migration with the command: 

```bash
flask db upgrade
```

At the end set SECRET_KEY value in local .env file.

## Start
The application can be launched by running the start.bat file or command:

```bash
flask run
```
and typing http://127.0.0.1:5000/books/ or http://127.0.0.1:5000/hires/ into the address of any web browser.