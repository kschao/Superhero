from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'myapp'
urlpatterns = [
    path('index', views.index, name='index')
    path('<int:movie_id>/', views.details, name='detail')
]
