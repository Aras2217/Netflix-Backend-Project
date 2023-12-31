"""
URL configuration for netflix24ocak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from appMy.views import *
from appUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name="indexPage"),
    path('netflix/', indexBrowsePage, name="indexBrowsePage1"),
    path('netflix/<str:cate>', indexBrowsePage, name='indexBrowsePage2'),
    path('netflix/Listem', indexBrowsePage, name='indexBrowsePage3'),
    path('netflix/<pid>/', profileLogin, name="indexProfile"),

    # === USER ===
    path('profile/', profileUser, name="profileUser"),
    path('delete-profile/<pid>/', profileDelete, name="profileDelete"),
    path('account/', accountUser, name="accountUser"),
    path('login/', loginUser, name="loginUser"),
    path('register/', registerUser, name="registerUser"),
    path('logoutUser/cıkıs', logoutUser, name="logoutUser"),
    path('netflix/create_listem_category/<movie_id>/', create_listem_category, name='create_listem_category'),

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
