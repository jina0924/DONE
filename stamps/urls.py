from django.urls import path
from . import views

app_name = 'stamps'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('calendar/', views.calendar, name='calendar'),
    path('<int:goal_pk>/create_daily/', views.create_daily, name='create_daily'),
]