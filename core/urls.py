from django.urls import path	
from .views import *

urlpatterns = [
	path('', Index, name="index"),
	path('aboutus', aboutUs, name="aboutus"),
	path('Team/', Member, name="member"),
	path('contact/', Contact, name="contact"),
	
]