[![Django CI](https://github.com/ReggieReo/ku-polls/actions/workflows/django.yml/badge.svg)](https://github.com/ReggieReo/ku-polls/actions/workflows/django.yml)
## KU Polls: Online Survey Questions 

An application to conduct online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install

For installation instructions, please refer to [Installation.md](./Installation.md).

##  Run

Create a Virtual Environment and Install Dependencies before running the app

Navigate to the project directory:
```bash
cd [YOUR_PROJECT_NAME]
```
Create a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
* Linux/macOS:
```bash
source venv/bin/activate
```
* Windows:
```bash
.\venv\Scripts\activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

To run the app
```bash
python ./manage.py runserver
```


## Demo Super Users

|   Username  | Password        |
|-------------|-----------------|
|   reoreggie   | 1234 |

## Demo Users
|   Username  | Password        |
|-------------|-----------------|
|   EXUser1   | EXPass1 |
|   EXUser2   | EXPass2 |

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Development Plan](../../wiki/Development%20Plan)
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Task Board](https://github.com/users/ReggieReo/projects/1/views/2)
- [Iteration 2 Plan](../../wiki/Iteration%202%20Plan) and [Task Board](https://github.com/users/ReggieReo/projects/1/views/3)
- [Iteration 3 Plan](../../wiki/Iteration%203%20Plan) and [Task Board](https://github.com/users/ReggieReo/projects/1/views/4)

[django-tutorial]: (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
