from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
{%- if cookiecutter.use_async == 'y' %}
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
{%- endif %}
from django.urls import include, path, re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from {{ cookiecutter.project_slug }}.search import views as search_views  # noqa isort:skip

urlpatterns = [
    path("", TemplateView.as_view(template_name="home/home_page.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% raw %}{% url "admin:index" %}{% endraw %}
    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
    # Wagtail Admin
    path(settings.WAGTAIL_ADMIN_URL, include(wagtailadmin_urls)),
    re_path(r"^documents/", include(wagtaildocs_urls)),
    re_path(r"^search/$", search_views.search, name="search"),
    # User management
    path("users/", include("{{ cookiecutter.project_slug }}.users.urls", namespace="users")),
    path("", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail’s page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
{%- if cookiecutter.use_async == 'y' %}
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
{%- endif %}

if settings.DEBUG:
    # Wagtail settings: Serve static and media files from development server
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
