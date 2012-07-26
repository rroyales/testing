from django.conf.urls import patterns, include, url
from login.views import *
# import that directly goes to template no views needed
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',
	(r'^$', main_page),
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),
	(r'^direct/$', direct_to_template, {'template': 'direct.html'}),
	(r'^beers/$', 'beer.views.BeersAll'),
	(r'^beers/(?P<beerslug>.*)/$', 'beer.views.SpecificBeer'),
	(r'^brewerys/(?P<breweryslug>.*)/$', 'beer.views.SpecificBrewery'),
    # Examples:
    # url(r'^$', 'chapter10.views.home', name='home'),
    # url(r'^chapter10/', include('chapter10.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
