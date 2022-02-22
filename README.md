.. image:: https://img.shields.io/github/workflow/status/Jean-Zombie/cookiecutter-django-wagtail/CI/master
:target: https://github.com/Jean-Zombie/cookiecutter-django-wagtail/actions?query=workflow%3ACI
:alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
:target: https://github.com/ambv/black
:alt: Code style: black

# Cookiecutter Django Wagtail

Cookiecutter-Django-Wagtail is a fork of the awesome `Cookiecutter Django`_ combined with `Wagtail`_.

- Cookiecutter Django Documentation: https://cookiecutter-django.readthedocs.io/en/latest/
- Wagtail Documentation: https://docs.wagtail.io/en/stable/
- See Troubleshooting\_ (Cookiecutter Django) for common errors and obstacles

.. \_Wagtail: https://wagtail.io/
.. \_Troubleshooting: https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html
.. \_Cokkiecutter: https://github.com/audreyr/cookiecutter.git
.. \_Cookiecutter Django: https://github.com/pydanny/cookiecutter-django.git

## Features

- For Django 3.1
- **Wagtail 2.14**
- Works with Python 3.9
- Renders Django projects with 100% starting test coverage
- Twitter Bootstrap* v5 (`maintained Foundation fork`* also available)
- 12-Factor* based settings via django-environ*
- Secure by default. We believe in SSL.
- Optimized development and production settings
- Comes with custom user model ready to go
- Optional basic ASGI setup for Websockets
- Optional custom static build using Gulp and livereload
- Send emails via Anymail* (using Mailgun* by default or Amazon SES if AWS is selected cloud provider, but switchable)
- Media storage using Amazon S3 or Google Cloud Storage
- Docker support using docker-compose* for development and production (using Traefik* with LetsEncrypt\_ support)
- Procfile\_ for deploying to Heroku
- Instructions for deploying to PythonAnywhere\_
- Run tests with unittest or pytest
- Customizable PostgreSQL version
- Default integration with pre-commit\_ for identifying simple issues before submission to code review

.. \_`maintained Foundation fork`: https://github.com/Parbhat/cookiecutter-django-foundation

## Optional Integrations

_These features can be enabled during initial project setup._

- Serve static files from Amazon S3, Google Cloud Storage or Whitenoise\_
- Configuration for Celery* and Flower* (the latter in Docker setup only)
- Integration with MailHog\_ for local email testing
- Integration with Sentry\_ for error logging

.. \_Bootstrap: https://github.com/twbs/bootstrap
.. \_django-environ: https://github.com/joke2k/django-environ
.. \_12-Factor: http://12factor.net/
.. \_django-allauth: https://github.com/pennersr/django-allauth
.. \_django-avatar: https://github.com/grantmcconnaughey/django-avatar
.. \_Procfile: https://devcenter.heroku.com/articles/procfile
.. \_Mailgun: http://www.mailgun.com/
.. \_Whitenoise: https://whitenoise.readthedocs.io/
.. \_Celery: http://www.celeryproject.org/
.. \_Flower: https://github.com/mher/flower
.. \_Anymail: https://github.com/anymail/django-anymail
.. \_MailHog: https://github.com/mailhog/MailHog
.. \_Sentry: https://sentry.io/welcome/
.. \_docker-compose: https://github.com/docker/compose
.. \_PythonAnywhere: https://www.pythonanywhere.com/
.. \_Traefik: https://traefik.io/
.. \_LetsEncrypt: https://letsencrypt.org/
.. \_pre-commit: https://github.com/pre-commit/pre-commit

## Constraints

- Registration via django-allauth\_ not implemented (unlike the OG Cookiecutter Django)
- Only maintained 3rd party libraries are used.
- Uses PostgreSQL everywhere (10.16 - 13.2)
- Environment variables for configuration (This won't work with Apache/mod_wsgi).

## Usage

Instead of using Wagtail’s :code:`start` command you will use Cookiecutter to set up your project. Cookiecutter will prompt you for some technical and administrative question like your name, email, and various configuration issues.

Install Cookiecutter first::

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo::

    $ cookiecutter https://github.com/Jean-Zombie/cookiecutter-django-wagtail/

You'll be prompted for some values. Provide them, then a Wagtail project will be created for you.

For local development, see the following:

- `Developing locally`\_
- `Developing locally using docker`\_

.. _options: http://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html
.. _`Developing locally`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html
.. \_`Developing locally using docker`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html

## Support Cookiecutter Django!

The upstream of this repo, i.e. _Cookiecutter Django_, is run by volunteers. Please support them in their efforts to maintain and improve Cookiecutter Django:

- Daniel Roy Greenfeld, Project Lead (`GitHub <https://github.com/pydanny>`_, `Patreon <https://www.patreon.com/danielroygreenfeld>`_): expertise in Django and AWS ELB.

- Nikita Shupeyko, Core Developer (`GitHub <https://github.com/webyneter>`\_): expertise in Python/Django, hands-on DevOps and frontend experience.

## Code of Conduct

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`\_.

.. \_`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
