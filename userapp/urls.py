
from django.urls import path
from .views import HomeView

app_name = 'userapp'
urlpatterns = [
    path('', HomeView.as_view(), name='homeview'),

]