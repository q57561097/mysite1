from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views

urlpatterns = [
    url(r'^$',learn_views.index),
    url(r'^admin/',admin.site.urls)
]
