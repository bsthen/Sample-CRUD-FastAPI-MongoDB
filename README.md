### Sample CRUD FastAPI with MongoDB ###

## Introduction
I'm going to build a sample CRUD with FastAPI and MongoDB.
Using this sample to understand how to connect FastAPI with MongoDB.

## Installations

```sh
git clone https://github.com/bsthen/sample_crud_fastapi-mongodb.git && cd sample_crud_fastapi-mongodb
```

```sh
python3 -m venv env
``` Or looking for install virtual envirometns [link here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

```source env/bin/activate``` For linux or macOS

```\env\Scripts\activate.bat``` For windows

```pip3 install -r requirements.txt```

## Running the application

```uvicorn main:app --reload```

Open http://localhost:8000/docs/

## Database

please copy sample.env and rename it to .env and replace your mongodb connection url.