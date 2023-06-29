# Stock Market Data Analysis

This project aims to analyze and visualize stock market data using Django and Python.

## Features

- Fetches stock market data from a CSV file.
- Stores the data in a mysql database.
- Provides a web interface to view and search stock data.
- Offers data visualization using charts and graphs.

## Installation

1. Clone the repository:git clone `https://github.com/python-hacked/Insert-csv-data-DB.git`


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your-database-name',
        'USER': 'your-database-username',
        'PASSWORD': 'your-database-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

python manage.py migrate
python manage.py runserver
http://localhost:8000/

