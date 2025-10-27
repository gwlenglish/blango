"""
URL Configuration for the project.

The `urlpatterns` list routes URLs to views.

For more information:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

import blog.views
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("ip/", blog.views.get_ip),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
