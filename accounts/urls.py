
from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),  
    path('register/', RegisterView.as_view(), name='register'),
    path('success/', SuccessView.as_view(), name='success'),
    path('logout/',Logout.as_view(),name='logout'),

    path('detailregister/', Detailed_Registration.as_view(), name='detailregister'),

    


]