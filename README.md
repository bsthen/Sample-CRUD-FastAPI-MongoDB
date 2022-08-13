### Sample CRUD FastAPI with MongoDB ###

## Introduction
We are going to build a CRUD application with FastAPI and MongoDB.
Using sample to understand how to use FastAPI and MongoDB.

## Installations

```git clone https://github.com/bsthen/sample_crud_fastapi-mongodb.git && cd sample_crud_fastapi-mongodb```

```python3 -m venv env``` Or looking for install virtual envirometns [link here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

```pip install -r requirements.txt```

```source env/bin/activate``` For linux or macOS

```\env\Scripts\activate.bat``` For windows

```pip3 install -r requirements.txt```

## Running the application

```uvicorn main:app --reload```

Open http://localhost:8000/docs/

## Database

please copy sample.env and rename it to .env