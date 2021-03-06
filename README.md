# Bikezon [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://bikezon.pythonanywhere.com/)

- [Info about API keys and email server](#note-on-api-keys-for-email-and-recaptcha)
- [Set up](#getting-started)
- [Prerequisties](#installing-dependencies-and-initialising-the-project)
- [Deployment with docker](#using-the-provided-dockerfile)
- [Hosting](#hosting-and-access-to-website)
- [Running tests](#running-tests)
- [Acknowledgements](#built-with)

<https://bikezon.pythonanywhere.com/>

Django based website that will allow users to participate in an online bicycle and parts marketplace. Users will be able to create accounts, postings, browse categories and book items to buy. The marketplace will specifically focus on bikes and parts for them.

## Note on API keys for email and reCAPTCHA

The email API and reCAPTCHA API use keys that **will not** be provided with the repo. These keys however, exist in production, so you can see the
fully working features there. **Instead** for development, the email will print the email that would be sent to local output and reCAPTCHA uses test
API key that means the captcha is always complete. Again, **these fully work in production**. If you would like for these to work on your own machine,
you can provide your own reCAPTCHA key and your **gmail** email and password. The email credentials must be provided in json format. If the server finds the json
then it will use that email instead. In order for this to work, less secure apps have to be enabled on the gmail account.

## Getting started

In order to setup the project on your local machine:

Open a terminal and change into the directory that you wish to work in (for the example this will be workspace).

Using anaconda to create virtual-env and clone repo:

```shell
(base)workspace$:conda create -n bikezon python=3.6.5
(base)workspace$:conda activate bikezon
(bikezon)workspace$:conda install pip
(bikezon)workspace$:git clone https://github.com/bikezon/bikezon.git
```

You can use any other virtual environment if you would prefer to.

## Installing dependencies and initialising the project

Dependencies for the project can be found in requirements.txt.

In order to setup the project on windows:

```shell
(bikezon)workspace$:start init.bat
```

And let the batch file run. After it is done you can close it. This will install all dependencies, initialise the database and populate the database.
This also creates a super user:

```shell
username: admin
password: admin
```

In order to setup the project on linux:

```shell
(bikezon)workspace$: ./init.sh
```

The script will do the same thing as on the windows version.

All dependencies are installed **inside of your virtual environment** - so there is no need to use the --user flag unless you are setting up the project outside of a virtual environment (not reccommended).

To run the project locally use:

```shell
(bikezon)workspace$:python manage.py runserver
```

And go to 127.0.0.1:8000 in your browser.

## Using the provided Dockerfile

On Linux:

Requires docker and docker-compose.

```shell
workspace$: git clone https://github.com/bikezon/bikezon.git
workspace$: cd bikezon
workspace/bikezon$: sudo docker-compose up
```

And go to 127.0.0.1:8000 in your browser.

On Windows:

Get docker and docker-compose for windows: <https://docs.docker.com/docker-for-windows/>

```shell
workspace$: git clone https://github.com/bikezon/bikezon.git
workspace$: cd bikezon
workspace/bikezon$: docker-compose up
```

And go to 127.0.0.1:8000 in your browser.

## Hosting and access to website

[Check out the website](https://bikezon.pythonanywhere.com/)

## Running tests

In order to run the test file for the project the [geckodriver](https://github.com/mozilla/geckodriver/releases "geckodriver") has to be installed. In order to install the driver follow the instructions on the geckodriver github repo
(see link). On windows geckodriver must also be added to your PATH variable. The [Mozilla Firefox](https://www.mozilla.org/en-GB/firefox/new/ "Mozilla Firefox") web browser is required.
In order to launch the tests run the test file:

First, clean the database:

Windows

```shell
(bikezon)workspace$: start clean_db.bat
```

Linux

```shell
(bikezon)workspace$: ./clean_db.sh
```

After the database is clean, run the tests (this may take a while):

```shell
(bikezon)workspace$: python tests.py
```

Test results are logged into logs/test_logs.log

## Built with

[Django](https://www.djangoproject.com/ "Django's Homepage") - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

[Django Boostrap 4](https://pypi.org/project/django-bootstrap4/ "Bootstrap support for Django projects") - Bootstrap support for Django projects.

[Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) - django-crispy-forms provides you with a |crispy filter and {% crispy %} tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way.

[Pillow](https://pillow.readthedocs.io/en/stable/) - Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

[Django phone field](https://github.com/VeryApt/django-phone-field) - Lightweight model and form field for phone numbers in Django.

[jQuery](https://jquery.com/ "jQuery") - jQuery is a fast, small, and feature-rich JavaScript library.

[Google AJAX API](https://support.google.com/webmasters/answer/174993?hl=en) - a set of web development techniques using many web technologies on the client side to create asynchronous web applications.

[Google Search API](https://developers.google.com/custom-search/v1/overview) - The Custom Search JSON API lets you develop websites and applications to retrieve and display search results from Google Custom Search programmatically.

[reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display) - reCAPTCHA protects you against spam and other types of automated abuse. Here, we explain how to add reCAPTCHA to your site or application.

[Github Cards API](https://github.com/lepture/github-cards) - Card for your GitHub profile, card for your GitHub repositories.

[Selenium](https://www.selenium.dev/ "selenium") - Selenium is a portable framework for testing web applications.

[Coverage.py](https://coverage.readthedocs.io/en/coverage-5.0.3/ "coverage") - a tool for measuring code coverage of Python programs.

[geckodriver](https://github.com/mozilla/geckodriver/releases "geckodriver") - Proxy for using W3C WebDriver compatible clients to interact with Gecko-based browsers.
