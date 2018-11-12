
from django.conf.urls import url
from django.contrib  import admin

from .views import (
	index_call,
	grilla_call,
	contacto_call,
	detalle_call,
	)

urlpatterns = [

	url(r'^$', index_call, name = 'indexCall'),
	url(r'^productos/$', grilla_call, name = 'grilla'),	
	url(r'^contacto/$', contacto_call, name = 'contacto'),
	url(r'^detalle/$', detalle_call, name = 'detalle'),

]