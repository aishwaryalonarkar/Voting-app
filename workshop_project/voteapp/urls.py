"""workshop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('newparty/',views.new_party,name='newparty'),
    path('viewparty/',views.view_party, name='viewpartty'),
    path(r'viewparty/delete/<int:id>/',views.del_party,name='delete'),
    path('viewresults/',views.view_results, name='viewresults'),
    path(r'viewparty/viewinfo/<int:id>/', views.view_info, name='viewinfo'),
    path(r'viewparty/incvote/<int:id>/', views.inc_vote, name='incvote'),
    path(r'update/<int:id>/',views.ViewUpdatePost.as_view(),name='update'),
    path('winner/',views.declare_winner,name='winner'),
    path('jresp/',views.jresp,name='jresp'),
    #path('winner1/',views.declare_winner1,name='winner1'),

]
 