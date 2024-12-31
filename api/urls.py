from django.urls import path
from . import views
from .views import PasswordChangeView , UserInformationView

urlpatterns = [
    path('user' ,UserInformationView.as_view() , name = 'user-info'),
    path('change-password/', PasswordChangeView.as_view(), name='change-password'),

]
