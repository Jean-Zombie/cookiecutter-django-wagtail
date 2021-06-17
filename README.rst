.. image:: https://img.shields.io/github/workflow/status/Jean-Zombie/cookiecutter-django-wagtail/CI/master
    :target: https://github.com/Jean-Zombie/cookiecutter-django-wagtail/actions?query=workflow%3ACI
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black
    
    
Cookiecutter Django Wagtail
=======================

Cookiecutter-Django-Wagtail is a fork of the awesome `Cookiecutter Django`_ combined with `Wagtail`_. 


* Cookiecutter Django Documentation: https://cookiecutter-django.readthedocs.io/en/latest/
* Wagtail Documentation: https://docs.wagtail.io/en/stable/
* See Troubleshooting_ (Cookiecutter Django) for common errors and obstacles

.. _Wagtail: https://wagtail.io/
.. _Troubleshooting: https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html
.. _Cokkiecutter: https://github.com/audreyr/cookiecutter.git
.. _Cookiecutter Django: https://github.com/pydanny/cookiecutter-django.git

Features
---------

<<<<<<< HEAD
* For Django 3 (3.0.10)
* **Wagtail 2.11.3**
* Works with Python 3.8
=======
* For Django 3.1
* **Wagtail 2.13.1**
* Works with Python 3.9
>>>>>>> upstream/master
* Renders Django projects with 100% starting test coverage
* Twitter Bootstrap_ v4 (`maintained Foundation fork`_ also available)
* 12-Factor_ based settings via django-environ_
* Secure by default. We believe in SSL.
* Optimized development and production settings
* Registration via django-allauth_
* Comes with custom user model ready to go
* Optional basic ASGI setup for Websockets
* Optional custom static build using Gulp and livereload
* Send emails via Anymail_ (using Mailgun_ by default or Amazon SES if AWS is selected cloud provider, but switchable)
* Media storage using Amazon S3 or Google Cloud Storage
* Docker support using docker-compose_ for development and production (using Traefik_ with LetsEncrypt_ support)
* Procfile_ for deploying to Heroku
* Instructions for deploying to PythonAnywhere_
* Run tests with unittest or pytest
* Customizable PostgreSQL version
* Default integration with pre-commit_ for identifying simple issues before submission to code review

.. _`maintained Foundation fork`: https://github.com/Parbhat/cookiecutter-django-foundation


Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Serve static files from Amazon S3, Google Cloud Storage or Whitenoise_
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
.. _Traefik: https://traefik.io/
.. _LetsEncrypt: https://letsencrypt.org/
.. _pre-commit: https://github.com/pre-commit/pre-commit

Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (9.4 - 12.3)
* Environment variables for configuration (This won't work with Apache/mod_wsgi).

Usage
------

Instead of using Wagtail’s :code:`start` command you will use Cookiecutter to set up your project. Cookiecutter will prompt you for some  technical and administrative question like your name, email, and various configuration issues.

Install Cookiecutter first::

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo::

    $ cookiecutter https://github.com/Jean-Zombie/cookiecutter-django-wagtail/
    
You'll be prompted for some values. Provide them, then a Wagtail project will be created for you.

For local development, see the following:

* `Developing locally`_
* `Developing locally using docker`_

.. _options: http://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html
.. _`Developing locally`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html
.. _`Developing locally using docker`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html

Support Cookiecutter Django!
----------------------

The upstream of this repo, i.e. *Cookiecutter Django*, is run by volunteers. Please support them in their efforts to maintain and improve Cookiecutter Django:

* Daniel Roy Greenfeld, Project Lead (`GitHub <https://github.com/pydanny>`_, `Patreon <https://www.patreon.com/danielroygreenfeld>`_): expertise in Django and AWS ELB.

* Nikita Shupeyko, Core Developer (`GitHub <https://github.com/webyneter>`_): expertise in Python/Django, hands-on DevOps and frontend experience.


Code of Conduct
---------------

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.


.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
