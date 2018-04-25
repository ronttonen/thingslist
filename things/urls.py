
from django.conf.urls import url
from django.contrib import admin
from things.views import HomeView, CreateThing, ThingView, EditThing, ContactAuthor  
from things.ajax import CreateThingAjax, EditThingAjax, ContactAuthorAjax


urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^create/$', CreateThing.as_view()),
    url(r'^things/(?P<id>\d+)/$', ThingView.as_view()),
    url(r'^contact/(?P<id>\d+)/$', ContactAuthor.as_view()),
    url(r'^edit/(?P<slug>[-\w]+)/$', EditThing.as_view()),
    url(r'^ajax/create_thing$', CreateThingAjax.as_view()),
    url(r'^ajax/edit_thing$', EditThingAjax.as_view()),
    url(r'^ajax/contact_author$', ContactAuthorAjax.as_view())
]