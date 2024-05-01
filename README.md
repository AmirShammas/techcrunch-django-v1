# Techcrunch-Scraper

This app crawls into the [techcrunch](https://techcrunch.com) website using Django templates and sqlite database.

## Installation

This app is developed using python 3.11.

After making venv, install the necessary packages using the command below:

```
pip install -r requirements.txt
```

Copy `sample_settings.py` file and rename it to `local_settings.py`.

To generate the secret key, run the command below:

```
py -c "import secrets; print(secrets.token_urlsafe())"
```

Copy and paste this new value into the `local_settings.py` under the variable `SECRET_KEY`.

Run migrations:

```
py manage.py makemigrations

py manage.py migrate
```

Run the server:

```
py manage.py runserver
```

## Usage

In search url (localhost:8000/search/), you can scrape the website using keyword and page_count.

In plot url (localhost:8000/plot/), you can display article/author or article/tag plots.

## TODO

- [ ] Add django-import-export package
