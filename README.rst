Cookiecutter Django *Wagtail-Edition*
=======================

.. image:: https://travis-ci.org/pydanny/cookiecutter-django.svg?branch=master
    :target: https://travis-ci.org/pydanny/cookiecutter-django?branch=master
    :alt: Build Status

.. image:: https://pyup.io/repos/github/pydanny/cookiecutter-django/shield.svg
    :target: https://pyup.io/repos/github/pydanny/cookiecutter-django/
    :alt: Updates

.. image:: https://badges.gitter.im/Join Chat.svg
    :target: https://gitter.im/pydanny/cookiecutter-django?utm_sourc

.. image:: https://www.codetriage.com/pydanny/cookiecutter-django/badges/users.svg
    :target: https://www.codetriage.com/pydanny/cookiecutter-django
    :alt: Code Helpers Badge

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black

Cookiecutter-Django-Wagtail is a fork of the awesome Cookiecutter Django. 
Powered by Cookiecutter_, Cookiecutter Django is a framework for jumpstarting
production-ready Django projects quickly.

* Documentation: https://cookiecutter-django.readthedocs.io/en/latest/
* See Troubleshooting_ for common errors and obstacles
* If you have problems with Cookiecutter Django, please open issues_ don't send
  emails to the maintainers.

.. _Troubleshooting: https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html

.. _528: https://github.com/pydanny/cookiecutter-django/issues/528#issuecomment-212650373
.. _issues: https://github.com/pydanny/cookiecutter-django/issues/new

Features
---------

* For Django 2.0
* **Wagtail CMS 2.4**
* Works with Python 3.6
* Twitter Bootstrap_ v4.1.1 (`maintained Foundation fork`_ also available)
* 12-Factor_ based settings via django-environ_
* Secure by default. We believe in SSL.
* Optimized development and production settings
* Registration via django-allauth_
* Comes with custom user model ready to go
* Optional custom static build using Gulp and livereload
* Send emails via Anymail_ (using Mailgun_ by default, but switchable)
* Media storage using Amazon S3
* Docker support using docker-compose_ for development and production (using Caddy_ with LetsEncrypt_ support)
* Procfile_ for deploying to Heroku
* Instructions for deploying to PythonAnywhere_
* Run tests with unittest or py.test
* Customizable PostgreSQL version

.. _`maintained Foundation fork`: https://github.com/Parbhat/cookiecutter-django-foundation


Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Serve static files from Amazon S3 or Whitenoise_
* Configuration for Celery_ and Flower_ (the latter in Docker setup only)
* Integration with MailHog_ for local email testing
* Integration with Sentry_ for error logging

.. _Bootstrap: https://github.com/twbs/bootstrap
.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _django-allauth: https://github.com/pennersr/django-allauth
.. _django-avatar: https://github.com/grantmcconnaughey/django-avatar
.. _Procfile: https://devcenter.heroku.com/articles/procfile
.. _Mailgun: http://www.mailgun.com/
.. _Whitenoise: https://whitenoise.readthedocs.io/
.. _Celery: http://www.celeryproject.org/
.. _Flower: https://github.com/mher/flower
.. _Anymail: https://github.com/anymail/django-anymail
.. _MailHog: https://github.com/mailhog/MailHog
.. _Sentry: https://sentry.io/welcome/
.. _docker-compose: https://github.com/docker/compose
.. _PythonAnywhere: https://www.pythonanywhere.com/
.. _Caddy: https://caddyserver.com/
.. _LetsEncrypt: https://letsencrypt.org/

Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (9.2+)
* Environment variables for configuration (This won't work with Apache/mod_wsgi except on AWS ELB).

Usage
------

Instead of using ``startproject``you will use Cookiecutter to set up your project. Cookiecutter will prompt you for some  technical and administrative question like your name, email, and various configuration issues.

Install Cookiecutter first::

    $ pip install "cookiecutter>=1.4.0"

Now run it against this repo::

    $ cookiecutter https://github.com/Jean-Zombie/cookiecutter-django-wagtail/
    
You'll be prompted for some values. Provide them, then a Django project will be created for you.

For local development, see the following:

* `Developing locally`_
* `Developing locally using docker`_

.. _options: http://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html
.. _`Developing locally`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html
.. _`Developing locally using docker`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html


Code of Conduct
---------------

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.


.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
