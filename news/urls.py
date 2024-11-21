from django.urls import path
from .views import *

urlpatterns = [
    path('Lista-News/', ListNews, name="List-News"),
    path('detailnews/<str:hashid>', detailNews, name="detailnews"),
    path(' addnews/', addNews, name="addnews"),
    path(' Update-News/<str:hashid>', updateNews, name="update-News"),
    path(' Delete-News/<str:hashid>', DeleteNews, name="Delete-News"),
 
]