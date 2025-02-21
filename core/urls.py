from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from lib.utils.env import is_dev
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static


def is_dev():
    return settings.DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("url_shortner.urls"))
]

if is_dev():
    urlpatterns += debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])