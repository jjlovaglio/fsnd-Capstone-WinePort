# WinePort

## Introduction

WinePort is a winery and winemaker booking site that facilitates the discovery and bookings of wines between local winemakers and wineries. This site lets you list new winemakers and wineries, discover them, and list wines with winemakers as a winery owner.

### Motivation

The motivation for this project is to build a prototype to test the feasibility of a social platform that will bring online the interactions and flow of information for actors of the wine industry.

## Project Dependencies
### Backend
#### main dependencies:
* **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** 
 * **PostgreSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 * **Flask-Migrate** for creating and running schema migrations
* **python-jose-cryptodome** for decoding JWT's

You can download and install these and all other required dependencies using `pip` as:
```
pip install -r requirements.txt
```
> **Note** - If I do not mention the specific version of a package, then the default latest stable package will be installed. 

### Frontend
Fontend consists of html, css and `Jinja2` templating

## Project Structure
#### Main files
  ```sh
  ├── static
  ├── css 
  ├── font
  ├── ico
  ├── img
  ├── js
  ├── errors
  ├── forms
  ├── layouts
  ├── pages
  ├── auth.py
  ├── error.log
  ├── run.py *** the main app. Includes SQLALchemy models
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── db_populate.py
  ├── forms.py *** All custom forms
  ├── README.md
  ├── requirements.txt *** The dependencies to install with `pip3 install -r requirements.txt`
  └── setup.sh *** environment variables 
  ```

Overall:
* Models are located in the `MODELS` section of `run.py`.
* Controllers are also located in `run.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.
* Web forms for creating data are located in `form.py`


Highlight folders:
* `templates/pages` -- Defines the pages that are rendered to the site. These templates render views based on data passed into the template’s view, in the controllers defined in `run.py`. These pages successfully represent the data to the user.
* `templates/layouts` -- Defines the layout that a page can be contained in to define footer and header code for a given page.
* `templates/forms` -- Defines the forms used to create new winemakers, wines, and wineries.
* `run.py` -- Defines routes that match the user’s URL, and controllers which handle data and renders views to the user. 
* Models in `run.py` -- Defines the data models that set up the database tables.
* `config.py` -- Stores configuration variables and instructions, separate from the main application code. 

## Local Development

### Running the development server
1. Create a virtual environment
2. Install project dependencies

```
pip install -r requirements.txt 
```

### Creating the Database
3. Create a new Postgres development and testing database in CLI
```
psql createdb <database_name> && psql createdb <test_database_name>
```
4. Connect the databases to the project by updating DATABASE_URL and TEST_DATABASE_URL variables in `setup.sh`
5. Add environment variables to bash session
```
source setup.sh
```
6. Make sure you are using the development config settings by setting APP_SETTINGS variable in setup.sh to `config.DevelopmentConfig`
7. Run database migrations to create schema on psql
```
python manage.py db upgrade
```

### Populating the Database Locally
7. Populate the database
```
python db_populate.py
```

8. Run flask
```
flask run
```

## Running Tests Locally
1. switch to testing mode:
```
export APP_SETTINGS=config.TestingConfig
```
2. run tests
``` 
python tests.py
```

## Hosting 
App is hosted in `Heroku` at:

[https://fsnd-capstone-wineport.herokuapp.com/](https://fsnd-capstone-wineport.herokuapp.com/) 


## API behavior and RBAC controls

| | User 1 | User 2 |
| ---  | --- | --- |
| Role | WinePort Manager | Winemaker |
| Permissions | delete:winery edit:wine edit:winemaker edit:winery post:wine post:winemaker post:winery | edit:wine post:wine |

## Valid JWT tokens for Code Review
User 1 token: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExcTh6NHhFay1zSjJ0WnpXa3A2aSJ9.eyJpc3MiOiJodHRwczovL2pqbG92YWdsaW8udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMmE3YzQxNWVhZTg2MDA2OGU0MjUwMSIsImF1ZCI6IndpbmVwb3J0IiwiaWF0IjoxNjE5MTI1MzgyLCJleHAiOjE2MTkyMTE3ODIsImF6cCI6IjZGRGpZWHpxNEVzUzJ0NVpWQ1Y3YXJFWnVDMHEwSFBFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6d2luZXJ5IiwiZWRpdDp3aW5lIiwiZWRpdDp3aW5lbWFrZXIiLCJlZGl0OndpbmVyeSIsInBvc3Q6d2luZSIsInBvc3Q6d2luZW1ha2VyIiwicG9zdDp3aW5lcnkiXX0.J6I75Ck5gy5A43afT17doxivnZT-6sYYUSkT5ejB9wz34FoZbbuRQpl6HDM0PIP_DAhm_GtxYgOp3aSK7Gl6KH3a1ApzI7uw9s2e9g0eKCWAuIiv0wR0K90cR2y28ecZWmlzzpNsEwrgM4mlDP1ngEVP93Xd6Bz25OSj2NW_07_oicCrcQ8qyY83pmAxroXAoJ490e-AXSZj6z41nUTuDBW5JAIMm-uC6GsIX7aS1WCnMtcQV6P0Vp4dsvEmhCZBrUozxeVCf7AyO6XcPDN3Y1JdnAxFYQTB9CNvPC8dfF4y_qIOcNSYJc4b9di8nadJk_IZiZc7M1_GeMnE_mTuQw`

User 2 token:
`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExcTh6NHhFay1zSjJ0WnpXa3A2aSJ9.eyJpc3MiOiJodHRwczovL2pqbG92YWdsaW8udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMmE3YzZhNWVhZTg2MDA2OGU0MjUwYyIsImF1ZCI6IndpbmVwb3J0IiwiaWF0IjoxNjE5MTI1NDU1LCJleHAiOjE2MTkyMTE4NTUsImF6cCI6IjZGRGpZWHpxNEVzUzJ0NVpWQ1Y3YXJFWnVDMHEwSFBFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJlZGl0OndpbmUiLCJwb3N0OndpbmUiXX0.FXLrC51n8Lmz_fvVNPW22yRHxsplPiafgh8aE5Kx_keJGPnldYHZrppbFTB2XhbuDQP3AABuFIkRLhZRJVMhSuCzdMGvBrF49zkGbB55XhNfUxIy61N_WT85ImZyg39R1Kv3srkQoXuADb9d3LyBnjsTJ0-_xSsGNOaB8Q62pcHt8ZaNQeN8IReIpIJU59JdMUVgkA6CaMnxR1bR5N6LhbDCs9LMoU1hvOmtvuouwTzHaoTB6FF8qRE9f6NKYVJFyI-AC4koZ9YIA_8Ovy2YgPIt_xv22RNSTz_ldwEUkkzDWPHpbDTa-qko1VC8fCmHEQQuEiF20BBY2TPhTNR9Xw`

You can check the token's content at [jwt.io](https://jwt.io/)