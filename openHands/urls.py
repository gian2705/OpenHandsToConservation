from django.urls import path

from . import views

app_name = 'openHands'

urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('about', views.about_view, name='about'),
    path('volunteers', views.volunteers_view, name='volunteer'),
    path('members', views.members_view, name='members'),
    path('news', views.news_view, name='news'),
    path('projects', views.projects_view, name='projects'),
    path('post-create', views.post_create, name='createPost'),
    path('login', views.login_view, name='login')
]