# Installation Guide

### Clone or Download the Code

```bash
git clone https://github.com/ReggieReo/ku-polls.git
```
if you don't have git installed or prefer to download the code as a ZIP file, you can do so from the main apage of the repository by clicking on the `Code` button and then `Download ZIP`.

### Create a Virtual Environment and Install Dependencies

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

### Set Values for Externalized Variables
Using a providing .env file
```bash
mv sample.env .env
```

### Run Migrations
To set up your database schema, run:
```bash
python manage.py migrate
```

### Run Tests
Before starting the app, it's a good idea to run the tests to ensure everything is working as expected:
```bash
python manage.py test
```

### Install Data from Data Fixtures
Install data fixtures to populate your database with initial data:
```bash
python manage.py loaddata data/polls-question-v3.json
python manage.py loaddata data/polls-choice-v3.json
python manage.py loaddata data/users.json
```