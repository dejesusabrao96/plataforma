from django.urls import path
from .views import *

urlpatterns = [
	path('actividade/', Actividade, name="actividade"),
	path('addactividade/', addActivity, name="addactividade"),
	path('detailactivity/<str:hashid>', detailActivity, name="detailactivity"),
	path('updateactivity/<str:hashid>', updateActivity, name="updateactivity"),
	path('deleteactivity/<str:hashid>', DeleteActivity, name="deleteactivity"),
	path('report/', Report, name="report"),
    
]