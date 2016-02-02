# Basic template for a Python API with Flask

## About

This template is very simple. Basic URL routing. Plus, it makes a SPARQL query and formats the results in JSON. All in Python 3.4.


## Installation

Create a virtual environment with Python3.4 and launch it.

```bash
virtualenv -p /usr/bin/python3.4 venv
source venv/bin/activate
```

Install the required libraries.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Run the code.

```bash
python api.py
```

Exit the virtual environment.

```bash
deactivate
```