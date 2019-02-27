
.. image:: https://travis-ci.com/Jean-Zombie/cookiecutter-django-wagtail.svg?token=p8pxxXak7Km36T3knwF2&branch=master
    :target: https://travis-ci.com/Jean-Zombie/cookiecutter-django-wagtail
    :alt: Build Status
    
    
Cookiecutter Django Wagtail
=======================

Cookiecutter-Django-Wagtail is a fork of the awesome `Cookiecutter Django`_ combined with the `Wagtail CMS`_. 


* Cookiecutter Django Documentation: https://cookiecutter-django.readthedocs.io/en/latest/
* Wagtail Documentation: https://docs.wagtail.io/en/stable/
* See Troubleshooting_ (Cookiecutter Django) for common errors and obstacles
* If you have problems with Cookiecutter Django, please open issues_ don't send
  emails to the maintainers.

.. _Wagtail CMS: https://wagtail.io/
.. _Troubleshooting: https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html
.. _Cokkiecutter: https://github.com/audreyr/cookiecutter.git
.. _Cookiecutter Django: https://github.com/pydanny/cookiecutter-django.git
.. _issues: https://github.com/Jean-Zombie/cookiecutter-django-wagtail/issues

Disclaimer
---------
This is my first fork of anything. So I don't consider it production-ready. The build passes all tests but I most likely oversaw something. Specifically the compatibility to Django Version 2.1 needs further testing.

Features
---------

* For Django 2.1
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
