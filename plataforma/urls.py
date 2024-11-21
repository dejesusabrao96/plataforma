"""
URL configuration for plataforma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls.static import static
from plataforma import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('main.urls')),
    path('utilizador/', include('users.urls')),
    path('activity/', include('Activity.urls')),
    path('news/', include('news.urls')),
    path('project-implementation/', include('project_implementation.urls')),
    path('froala_editor/', include('froala_editor.urls')),
    path('login/', views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)