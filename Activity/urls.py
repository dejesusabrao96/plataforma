from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'actividade', ActivityViewSet)

urlpatterns = [

	path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

	path('actividade/', Actividade, name="actividade"),
	path('addactividade/', addActivity, name="addactividade"),
	path('detailactivity/<str:hashid>', detailActivity, name="detailactivity"),
	path('updateactivity/<str:hashid>', updateActivity, name="updateactivity"),
	path('deleteactivity/<str:hashid>', DeleteActivity, name="deleteactivity"),
	path('report/', Report, name="report")
    
]