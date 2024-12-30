# E-tanulás

## Install

## Setup

### Új tantárgy:

  Admin - Subjects - Add Subject



## Dev

Lokális fejlesztés

Backend:
```shell
git clone git@github.com:Alphaws/e-learn.git
cd e-learn backend
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser --username admin --email admin@noreply.com
./manage.py runserver
``` 
Test: http://localhost:8000/admin/

Frontend:

```shell
cd ../frontend
ng serve --open
```
Test: http://localhost:4200/
