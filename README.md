# Sample CRUD FastAPI with MongoDB #

## Introduction
I'm going to build a sample CRUD with FastAPI and MongoDB.
Using this sample to understand how to connect FastAPI with MongoDB.

## Installations

```sh
git clone https://github.com/bsthen/Sample-CRUD-FastAPI-MongoDB.git && cd Sample-CRUD-FastAPI-MongoDB
```

Create a virtual environment:
```sh
python3 -m venv env
``` 
Or looking for install virtual envirometns [link here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Activate ENV for Linux or macOS
```sh
source env/bin/activate
```
Or

Activate ENV for Windows
```sh
\env\Scripts\activate.bat
``` 
Install Dependencies
```sh
pip3 install -r requirements.txt
```

## Run the application

```sh
uvicorn main:app --reload
```

Open http://localhost:8000/docs/

## Database

please copy sample.env and rename it to .env and replace your mongodb connection url.
